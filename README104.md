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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3de2973d-fc25-3640-82b2-2f94bc4998da | -11.875 | -47.5902 | 2026-09-18 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| fa7153e6-bc25-3b26-9be4-9137d72bb3a9 | -7.0352 | -44.6396 | 2026-09-18 14:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 333ee917-d7a0-3645-9453-79b6162fb0b0 | -8.5425 | -44.5363 | 2026-09-18 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 15a32981-1ca2-3cdd-a7f6-e515bfeccd68 | -9.6016 | -45.8777 | 2026-09-18 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 196.1 |
| 140c731b-4c40-3566-ae48-5caaf199f2ea | -7.803 | -44.888 | 2026-09-18 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| bb11c132-e301-30f2-9c32-aa8377c716e7 | -8.2803 | -50.8653 | 2026-09-18 14:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 5fe1b486-034a-3c22-ae4f-c23d93b7c840 | -10.6536 | -50.4778 | 2026-09-18 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 1d4eb2dc-79e8-3e35-99f4-a289b023203e | -2.4999 | -49.4204 | 2026-09-18 14:50:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 89043543-82a3-3767-a777-88bc9a484e91 | -0.5442 | -49.1324 | 2026-09-18 14:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| a82b6751-830e-3fab-87ae-d1372e4dc952 | -9.5505 | -45.4752 | 2026-09-18 14:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| a653445c-5b24-3eb4-b15a-67dfc9ee0e59 | -6.3287 | -55.2677 | 2026-09-18 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 97435bb5-5ec4-3c8f-bc85-fe02fc361a9c | -14.1737 | -45.1641 | 2026-09-18 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 6165e4ca-d6fb-3c63-8b9e-77cdd1fb49c1 | -11.3625 | -44.0347 | 2026-09-18 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 5cfcd31e-0e50-376c-87fb-03b7f3a813ca | -7.1675 | -44.5589 | 2026-09-18 14:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 00a65214-d7ea-348f-87e5-cca65bfec987 | -6.6703 | -43.6337 | 2026-09-18 14:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 54744bd8-0cff-3e4d-8c0c-ee01a9c1ac97 | -10.6758 | -50.2406 | 2026-09-18 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 220.3 |
| 1ff4b0e5-1c1b-34cf-a74e-3bb14d3217a0 | -9.699 | -54.8176 | 2026-09-18 14:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| bd7bfdd9-5ffe-35de-90c4-8b5bcf91f2a1 | -11.8937 | -47.6099 | 2026-09-18 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 71f0b160-4bdb-30cd-98cf-d4424cfd750b | -7.8412 | -44.8385 | 2026-09-18 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 968ca2d3-8971-3eca-b0ab-2b703d99c1b6 | -6.745 | -45.483 | 2026-09-18 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 58fd94e7-c879-36ac-a682-7025b9923142 | -8.4503 | -45.8448 | 2026-09-18 14:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 9256911a-ea41-3abb-9d2f-5c4189bbb08f | -0.803 | -48.6611 | 2026-09-18 14:50:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 21296e75-346b-398b-9bd1-de91202e028d | -10.6944 | -50.26 | 2026-09-18 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 156.2 |
| e0f48999-1339-3898-9de3-5973ee2fd931 | -2.8101 | -50.4658 | 2026-09-18 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 2303d4f3-d023-36e7-8eb9-9e8c0f134ed5 | -2.4815 | -49.3996 | 2026-09-18 14:50:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| c3ddd19b-ff36-385c-9865-2664552dfa48 | -9.9509 | -46.6026 | 2026-09-18 14:50:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 2cef1706-4136-35cb-ac61-535486a978d8 | -11.9898 | -49.9413 | 2026-09-18 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 3f94ccad-f647-3161-a167-dcf942879d91 | -8.58 | -44.5552 | 2026-09-18 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 8e7ad1cc-9a49-3e05-bd72-1fc872833230 | -15.6752 | -52.7339 | 2026-09-18 14:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 126.7 |
| f3d91308-b6e1-3e55-a6ae-8df0cda1adbf | -7.8036 | -44.8422 | 2026-09-18 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 6cbb0681-dfd5-327e-aa41-12188e7afaf4 | -10.8186 | -50.8648 | 2026-09-18 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 64ff9c96-00c4-34d8-952e-05621fefd4b8 | -7.3564 | -44.4726 | 2026-09-18 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 82e7723e-fd3e-3170-a8b2-59d5a498ec02 | -9.8313 | -48.4073 | 2026-09-18 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| faeb9cf8-7393-3979-9efb-c06aa54caac7 | -8.9144 | -44.9774 | 2026-09-18 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c0483f99-7d9f-3636-8688-8921e81cb4d8 | -8.638 | -44.4567 | 2026-09-18 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 47cc68eb-ff3f-31ea-a860-23af91f73fac | -14.1594 | -48.751 | 2026-09-18 15:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 51ad0c99-c9bd-373f-b1c4-97c1897f406e | -11.2971 | -43.4088 | 2026-09-18 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| ce9bce4a-2029-33e1-a531-2f40ba9d4997 | -10.3303 | -45.3341 | 2026-09-18 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 6813da19-5501-377e-b600-9fd9ccaa17d6 | -9.7177 | -54.8162 | 2026-09-18 15:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 35de0763-b764-37ad-a552-1ec4ceec6506 | -7.8036 | -44.8422 | 2026-09-18 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 3ac4abcd-93f1-3744-98b9-b592e2b6cef0 | -14.1542 | -45.1675 | 2026-09-18 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 266.9 |
| 0162a50e-3722-3d39-82d7-6f9a99706584 | -0.5442 | -49.1324 | 2026-09-18 15:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| cd68173f-d563-3cca-ad74-b75249adf452 | -10.5178 | -46.7366 | 2026-09-18 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 856b5fa9-6b8c-3add-9287-eeb58af04867 | -9.2417 | -45.9185 | 2026-09-18 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| e5677126-8a81-38bc-9ae2-23f58d6f5f5f | -10.6758 | -50.2406 | 2026-09-18 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 169.4 |
| e3877076-e2b3-3f03-aed6-d91992fb1da7 | -2.0769 | -56.4085 | 2026-09-18 15:00:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 106ee084-1f55-3d6e-847d-6228c6dfb3f1 | -11.3809 | -44.0788 | 2026-09-18 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 0c4e275a-5d32-3839-860a-954c393066a7 | -12.0905 | -50.8307 | 2026-09-18 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 82b0f296-45f0-3ce4-825b-f84a57fc5fad | -10.6536 | -50.4778 | 2026-09-18 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 8a4f5789-2bb9-3917-9eb3-f88cb452f1dd | -8.3176 | -47.4842 | 2026-09-18 15:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 6fa8a38a-533f-3783-8165-dcc680cbd69d | -9.6816 | -48.3139 | 2026-09-18 15:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 0f4c8ae6-9f27-351f-82bc-ad21900c3f2c | -11.064 | -48.2898 | 2026-09-18 15:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 723475b0-1756-367b-8767-034fa72719b9 | -11.8359 | -50.046 | 2026-09-18 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 300c09ec-a51a-3a07-94cd-77673278e50d | -9.9136 | -46.5621 | 2026-09-18 15:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 3136e174-6eff-3834-9b2e-fd0b2065f24a | -11.3437 | -44.0141 | 2026-09-18 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 258.3 |
| c1fa41ac-a079-3cf2-a1e7-f88de476fd2b | -1.6042 | -54.415 | 2026-09-18 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b5209caa-a2e1-374b-b6fc-0516541242d3 | -10.6189 | -50.2466 | 2026-09-18 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 9ae512f2-6c70-3bdf-9233-9e6a0e2e2632 | -12.0238 | -51.4763 | 2026-09-18 15:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 2610bca9-5118-35da-9b9b-d9b7271468dd | -10.6525 | -50.5631 | 2026-09-18 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 5bea7495-a035-3b53-87cf-cb52bea705e8 | -12.0241 | -51.4551 | 2026-09-18 15:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 84750bd4-150e-385f-98b5-c6de00b59361 | -9.6019 | -45.855 | 2026-09-18 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 8626b5e2-9ba7-348f-8b60-f3360a334eda | -9.9956 | -50.2675 | 2026-09-18 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 8308a87a-ed2e-30f2-8223-3d55108322d0 | -0.803 | -48.6825 | 2026-09-18 15:00:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 85d0f649-0079-3562-a012-1b4d2762a652 | -10.6726 | -50.4758 | 2026-09-18 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 3b16d6e8-38b2-3bac-a6ce-598942146f75 | -9.5698 | -45.4501 | 2026-09-18 15:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 214b7281-72f2-301b-8f7a-3eb202595eb6 | -7.8038 | -44.8193 | 2026-09-18 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 546dc432-3f92-3b02-a6a2-35c9a5739f14 | -10.126 | -46.2899 | 2026-09-18 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 03c38392-302e-33fd-8be9-9008886a440f | -11.4541 | -51.4754 | 2026-09-18 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 150.6 |
| 445b405c-9be5-33e0-9783-1bdc37208b66 | -12.3591 | -50.7134 | 2026-09-18 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 7ccd0387-de40-3cac-91db-5ec7e3e71df5 | -10.3307 | -45.3112 | 2026-09-18 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 98d74fc1-fa6d-3c6b-b1b0-9e9aca50ae05 | -10.6533 | -50.4991 | 2026-09-18 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 41d27a44-5b3b-35c4-b0e2-9fc9e7031107 | -12.1448 | -44.243 | 2026-09-18 15:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| e4bf8a74-43fa-3cae-8d18-613b6e7c4afe | -2.4999 | -49.4204 | 2026-09-18 15:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| f5f05cdd-6cd5-3314-9c92-47a7278cb6d0 | -4.5961 | -42.95 | 2026-09-18 15:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 198.0 |
| 5ebb7b30-f0ef-3adf-8946-487cd2b9ead5 | -2.4999 | -49.3992 | 2026-09-18 15:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| dca5d27d-77e8-3c07-b1cf-a490b91cb13d | -9.699 | -54.8176 | 2026-09-18 15:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 83d8cd3d-b3b2-3549-a07f-d5d1b0e9f439 | -11.6423 | -51.5819 | 2026-09-18 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 75e6cb5b-da63-330a-9b2b-3605228f3594 | -8.6374 | -44.5029 | 2026-09-18 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| f0d57e19-6401-36d4-8fe4-64544b588428 | -7.8033 | -44.8651 | 2026-09-18 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 6775a305-1303-3d93-9e0c-2a7c2ebc7957 | -11.4167 | -51.4371 | 2026-09-18 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 391b7cb8-4c97-3314-8dce-52343c3d4764 | -3.9127 | -44.6505 | 2026-09-18 15:00:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| a23d3551-7eec-3c53-b4ca-7c77190436d9 | -14.1732 | -45.1875 | 2026-09-18 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 274.8 |
| 749d8a62-1ee1-3eb2-b2c8-5413d07e17cf | -11.8556 | -50.0006 | 2026-09-18 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| d9ded005-7df4-3e9f-90d6-5ba65b125055 | -11.875 | -47.5902 | 2026-09-18 15:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 169.5 |
| a9c99272-4142-3947-be68-98ee89142f90 | -8.5428 | -44.5132 | 2026-09-18 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 99ce1fd5-b901-3750-a993-1ec7a28b9e80 | -2.4814 | -49.4208 | 2026-09-18 15:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| e1b356b4-6a85-382e-9d63-58cc0cb46ffe | -11.3161 | -46.7699 | 2026-09-18 15:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 58696ef7-106a-30ad-840f-9049bd052b0e | -7.8563 | -45.1564 | 2026-09-18 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 177.0 |
| f429c408-beb3-3df7-91ec-10f61406a13a | -9.5505 | -45.4752 | 2026-09-18 15:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 108.8 |
| a1bd84a3-e201-39fb-b7d8-e63194d8c732 | -10.2821 | -50.0035 | 2026-09-18 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 8ea64875-caec-39fb-886b-bd1abd83a7fd | -9.8313 | -48.4073 | 2026-09-18 15:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| cffbccd6-a3fb-31c7-95cc-0cf3c4dc5657 | -11.8115 | -46.8158 | 2026-09-18 15:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 238.9 |
| 74dde677-e546-3e6b-936e-79183a5b7173 | -2.4815 | -49.3996 | 2026-09-18 15:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| f6e72868-1cdb-3fd4-9db5-35e2f2ddb03a | -7.841 | -44.8614 | 2026-09-18 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ac0bf14b-afc2-3a0d-b75a-078e34104b13 | -10.6379 | -50.2446 | 2026-09-18 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 3023c5f8-19a0-3a45-8707-72700a6aed9f | -11.3446 | -43.9671 | 2026-09-18 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 38250a99-face-3568-a3f8-e05541b2d4ac | -12.1256 | -44.246 | 2026-09-18 15:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 7f61e6e6-afc1-3f5e-b17e-52e41cb1c255 | -14.8026 | -48.5622 | 2026-09-18 15:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| d4f71421-c797-38c7-9c9a-c2cfa7cb3126 | -9.3251 | -48.1758 | 2026-09-18 15:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 5025805e-d8ea-3ba5-9e9f-18e47da154e5 | -1.2193 | -54.2192 | 2026-09-18 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |


[Clique aqui para ver as próximas entradas](README105.md)
