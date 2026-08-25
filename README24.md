# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94848d74-238e-38c9-828c-55c1bd0ef91e | -9.60105 | -45.37732 | 2026-08-25 04:08:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 487a9c9b-8d24-3354-8c64-35225e46873d | -12.84543 | -48.49606 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c95d60e-45f2-30b7-b54e-c92715977461 | -12.75359 | -46.45359 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74020911-552c-3dfb-9394-7118e8676d0a | -10.56474 | -50.43311 | 2026-08-25 04:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f68c55fb-dba3-3fb8-9bcb-cb202c0e1bc0 | -8.10023 | -47.47457 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 133e4440-78f5-34fb-9271-78aaf8433401 | -9.57725 | -49.23069 | 2026-08-25 04:08:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9505710c-6a66-340b-87f0-f2d078fa4ec4 | -9.53396 | -49.2741 | 2026-08-25 04:08:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e3f17f5-5c49-30a0-a6ac-8510fd98e348 | -13.10493 | -43.34771 | 2026-08-25 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 49f1f9e3-6087-3303-9e9e-5f078bc028ef | -9.36561 | -45.40973 | 2026-08-25 04:08:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7df4cb87-3b7d-3c95-99f1-c20f22652dba | -10.36844 | -45.06213 | 2026-08-25 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| c1cbd28a-d98a-3044-939f-7e33bf4050bd | -8.17038 | -46.70089 | 2026-08-25 04:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8c177a03-f4b9-3213-b2e0-4a7a07f3fddb | -13.44761 | -43.84865 | 2026-08-25 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 640fe477-e4d6-3cc0-8517-4fc7f9c746fc | -13.09023 | -43.3674 | 2026-08-25 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 425e6fcd-5363-3eed-a971-4d64fd45f105 | -12.2072 | -43.17579 | 2026-08-25 04:08:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 309ab8da-36ac-39f8-9f2a-4857b0aa9e7a | -10.31852 | -50.40377 | 2026-08-25 04:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21259b39-cba2-3466-a984-110b10dd85d2 | -8.15906 | -46.69464 | 2026-08-25 04:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9d2f1c2-cc45-3971-b410-7f4cfff740ef | -10.84999 | -50.55734 | 2026-08-25 04:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69a7d692-6418-332d-9168-bc725e682d1d | -12.78188 | -44.26819 | 2026-08-25 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 895e7358-e9fe-3c08-ad63-a8e61ae62a48 | -13.35497 | -48.20168 | 2026-08-25 04:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f50bc8bd-50eb-3a5a-b166-c0c373dc88ec | -8.07441 | -44.64653 | 2026-08-25 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ec1a8e6-ad7c-3be9-b357-d2da7348a098 | -8.07933 | -44.64328 | 2026-08-25 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 23d9adc6-2ec4-3649-af43-96e81eaa7d69 | -12.743 | -46.47923 | 2026-08-25 04:08:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7385d031-7a8e-3207-b048-4d2a4f78a625 | -8.09631 | -47.49641 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7210428f-7c8b-3215-aa78-7bb2280c8b57 | -8.17266 | -46.70275 | 2026-08-25 04:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af1003fe-7c76-3dc0-8798-ea2d51e34f4b | -12.14439 | -48.26087 | 2026-08-25 04:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9497e83-885e-3195-bd9c-db2b86bf18b5 | -8.76453 | -45.79561 | 2026-08-25 04:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10a57555-5436-34e2-bb31-04e0aa150e78 | -12.74484 | -46.46947 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 342d7a0b-0285-3395-a9cb-0391f9db98a9 | -13.09312 | -43.37239 | 2026-08-25 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd3cef2d-097a-38e9-a303-61bdf34e2a83 | -12.87632 | -48.49898 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cac167ef-4f42-3148-9e0f-dce07798937f | -10.36912 | -45.05825 | 2026-08-25 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 80806191-5515-3278-bec0-928973a260e8 | -10.05816 | -48.45522 | 2026-08-25 04:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fc61d5e3-2cd3-3db9-af7b-dafea7fb147c | -8.17363 | -46.6974 | 2026-08-25 04:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a65160b-5257-3d2f-bfb1-c284c7df0475 | -10.47485 | -50.43738 | 2026-08-25 04:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89de4933-b918-3f0d-8fe9-b6e124dbe3cb | -10.78803 | -50.93711 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fa5e3c35-3962-3baf-9f8b-a493033a1edb | -7.90107 | -46.38572 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd796543-04a5-37f5-b60f-a8012be6c8da | -12.74215 | -46.48375 | 2026-08-25 04:08:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e143b92a-e5a7-3f70-8187-2c6783df8ca9 | -10.78896 | -50.93236 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32f1590e-ce41-34ae-af21-f349292a361b | -10.91194 | -51.07306 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d16da88d-2841-37d1-970f-df0cff229faf | -13.36314 | -48.21226 | 2026-08-25 04:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b00cb64e-7379-30f7-8ce3-d59f3495335a | -6.83562 | -52.49816 | 2026-08-25 04:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2fdfea92-c282-3158-a8ec-83d1a1976793 | -12.71828 | -43.20513 | 2026-08-25 04:08:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 506f321a-185e-3774-8584-298d5ded2b9c | -12.14759 | -50.61183 | 2026-08-25 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 907814b6-ba0f-3abd-a587-94fb31e0a771 | -12.77889 | -44.26262 | 2026-08-25 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 60e604b8-186c-3ecf-aa3b-d6ccf66618cf | -12.20282 | -43.17937 | 2026-08-25 04:08:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a92c4732-a37d-37d1-9b6c-54b4475e6828 | -8.09504 | -47.47392 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7355f29-1d3c-3a28-b027-351dcca3bcca | -11.59918 | -46.75521 | 2026-08-25 04:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2537090-6eb6-3387-afd1-9871a6a4e5ff | -12.70629 | -48.41208 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 390e8001-04d4-3924-a533-658bd6b0b736 | -10.80321 | -50.923 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57f5e2d5-568a-3c37-a482-801483b46f52 | -9.3816 | -45.42115 | 2026-08-25 04:08:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ca4f21f-759a-317c-aca1-5ae5bb6a273e | -12.88141 | -48.49978 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86488b97-bc9a-3643-bf3d-ab35b9888756 | -6.9374 | -52.80008 | 2026-08-25 04:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f77c76fb-a5f3-3684-8193-e975077bd810 | -11.15869 | -54.00173 | 2026-08-25 04:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9376775e-74cb-3ca6-bdec-afa691bd30b4 | -12.88593 | -48.50354 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a73023f-ecb9-3db6-a191-c0dc3b505f34 | -8.66166 | -47.31694 | 2026-08-25 04:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff420db1-7661-34a0-9f4b-2f0028d0b79d | -13.09828 | -43.36438 | 2026-08-25 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75fdaae6-ab13-345b-9044-124d93dbbda4 | -11.01513 | -41.10027 | 2026-08-25 04:08:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 424073f6-34cf-3e8a-8efc-5a69615812a9 | -11.97388 | -45.89891 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b01e5f64-8985-32b7-87c1-3a20ddf66e96 | -10.37332 | -45.05902 | 2026-08-25 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 7d7ebf41-5317-3772-bd62-9eccd9be0f48 | -8.08425 | -44.64006 | 2026-08-25 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07e9123c-523f-3d2c-a589-55fd61793c7c | -12.13759 | -50.6008 | 2026-08-25 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75f11810-bbb4-3552-91ec-290adbd7fac5 | -8.07374 | -44.65046 | 2026-08-25 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 289395ae-8f21-39bc-982b-e2b8be32c7b3 | -13.34917 | -48.20535 | 2026-08-25 04:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 26412b7e-5120-39f3-8b98-218574569e0d | -8.92786 | -45.74634 | 2026-08-25 04:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a852ca0a-9f4c-32ef-ba17-d93244b022f5 | -12.21159 | -43.17207 | 2026-08-25 04:08:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f48c733f-4606-33f4-8cde-c87b02344425 | -12.84989 | -48.5001 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 635a547f-a41e-357e-8d0b-40cda774e86f | -12.87571 | -48.50216 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9df5e5a3-4ec1-357e-acfb-7bd512e44de4 | -8.07507 | -44.64262 | 2026-08-25 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3b9f1c5-2a84-3157-94dc-3709b1bb2f45 | -12.74391 | -46.47438 | 2026-08-25 04:08:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c215ed6-87fc-39d2-9a9e-661f86eb10d5 | -10.85595 | -50.55856 | 2026-08-25 04:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb045725-115e-33dc-ab6f-7fb20a032cfa | -12.71223 | -48.3911 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cc8f87e-bb75-350f-b62a-6105b17e1e76 | -10.03326 | -46.42576 | 2026-08-25 04:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6e7052f-297a-31d0-8ca3-1eebb016b814 | -11.44012 | -44.55384 | 2026-08-25 04:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcd257c6-54ed-3c02-8644-fcf25f970a36 | -12.7098 | -48.39412 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 15f4f6dd-20f9-3679-9ace-656719159fa5 | -11.98028 | -45.91306 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ae40a74-7b66-3ef3-95e3-990349efffa7 | -8.10146 | -47.49732 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee9e3e2d-c134-3b40-a3ff-6bc885aa114b | -11.13992 | -44.48225 | 2026-08-25 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 1c8ad6a2-f170-3809-a275-b094b58f2aee | -12.72163 | -48.38701 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5fdc5be-f512-3ec1-b82d-65ae3cee7948 | -13.35095 | -48.19611 | 2026-08-25 04:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33cdbf07-127b-3fa2-988e-c90f96c0aa18 | -8.15487 | -46.70338 | 2026-08-25 04:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad3d6392-e789-3e8f-82b1-104757408e31 | -11.98892 | -45.92199 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 877d950c-9b30-3679-98e2-3cd65f5fcc8a | -11.13684 | -44.47623 | 2026-08-25 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f53d0e42-ff71-361c-9489-e522271b3bc4 | -8.10541 | -47.47523 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f067628-e2f7-3c6c-8097-25724fbc6a53 | -12.87133 | -48.49765 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3880395-c4dc-34e2-b428-248174f6be0d | -13.35409 | -48.20628 | 2026-08-25 04:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 81384bcd-2094-3f7e-b85b-ad89d45d1344 | -10.48081 | -50.43861 | 2026-08-25 04:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8aa13780-bee3-3354-b659-b0f5a474942a | -8.08727 | -47.51711 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b674647-9823-3c81-9ea2-997fec3c4463 | -9.96408 | -48.32214 | 2026-08-25 04:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a42a6bbd-a096-3b02-bae7-5cfc2dbdcf96 | -9.5765 | -49.23464 | 2026-08-25 04:08:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf22be71-29e9-3dac-824f-025ca53c82a2 | -12.72291 | -48.38977 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bc68509-1f81-3a05-8825-d94d1965529e | -12.74592 | -46.47081 | 2026-08-25 04:08:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bec89984-eeb8-3d04-b3e7-9e0b8428b69d | -8.10597 | -47.47209 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80e28889-b286-3a49-93d4-6bc678abc39f | -6.93881 | -52.79284 | 2026-08-25 04:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3bfd6b78-31e0-3009-82b5-de19d8d8130d | -7.24998 | -49.85917 | 2026-08-25 04:08:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 267f1a49-77df-36b2-98d0-67de8e2f6cf4 | -7.90218 | -46.35666 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d8762a77-cdd0-3ab0-9990-3c9c4cad02d0 | -12.73706 | -46.4692 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d40bfe1a-1fa4-3ef9-9f59-fd5ba840e7a7 | -11.39124 | -45.1569 | 2026-08-25 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 93238b39-081f-38a2-9856-e0399ac8fb05 | -7.90105 | -46.3586 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 229abc89-aae5-376d-b96b-2c19a036ede9 | -11.39054 | -45.16076 | 2026-08-25 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8f83823f-779f-3f07-966b-dc9d037a1ae5 | -11.43273 | -44.5254 | 2026-08-25 04:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 865e8b24-76a9-34b6-b833-6d1b80643d98 | -8.06814 | -44.65762 | 2026-08-25 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README25.md)
