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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06238c64-6c43-336a-a6ed-60e32c80c934 | -8.05064 | -44.13557 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af94e589-bdbe-3653-a053-4bb75253dc70 | -6.25566 | -43.31422 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7dc81ef-cdf1-3753-ad57-27a5201593d2 | -7.26919 | -57.55602 | 2025-09-04 04:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4dd4a18b-d0c2-3814-ae76-4e119259ca1f | -6.88381 | -45.5624 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c58a62fb-fcae-395c-a74f-20906a4f5d26 | -9.43427 | -48.09623 | 2025-09-04 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 06455ba7-429d-3f82-87ba-33e62ae63feb | -6.67853 | -48.41417 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4e8eaba1-d11f-3126-b339-695e23c8344b | -6.78604 | -44.2953 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4054632-2ef5-3665-af04-99f87bed6d61 | -6.28368 | -43.50514 | 2025-09-04 04:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0b9c375-29e4-397f-9ee1-02d85d06e6aa | -6.33916 | -45.68365 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3748ba01-3b57-3082-ae08-538f97111081 | -6.30372 | -44.15491 | 2025-09-04 04:53:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 637d11b6-700e-3e67-b7d9-eed43543f171 | -8.08129 | -47.59142 | 2025-09-04 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62590e64-dd36-344d-a11d-4015f9224964 | -9.62767 | -47.08112 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 273bfad1-0e93-3d25-8280-317f2704f213 | -6.17293 | -47.28528 | 2025-09-04 04:53:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b179df5c-89e0-3243-a2b0-e2fafad8065e | -9.95914 | -51.64124 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4075b207-b925-3225-b1fc-66ec40defb20 | -7.74818 | -48.77171 | 2025-09-04 04:53:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c754af01-4364-33d7-ba52-e329a8fd5994 | -9.9711 | -51.63171 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74fdbee0-2efe-3fb3-a25d-b24379fe6d87 | -5.69536 | -45.94371 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2be5283-bd07-3c1a-9c29-f88309f763ba | -6.77911 | -63.14086 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f439146-566d-39f9-8ab7-6db2f6306bb9 | -5.6044 | -45.02319 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5a68435b-ae8f-364f-80d0-144dff62bb89 | -7.74435 | -48.77117 | 2025-09-04 04:53:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04a83884-9f5d-362a-a901-835cd7fc8816 | -10.03044 | -46.09706 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b393bb03-7876-3422-93a3-a7928744da8f | -5.82287 | -46.35914 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd0da399-fe8f-3ea4-8d01-f87838a83803 | -7.36335 | -44.32407 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7600d21-cd56-33d0-bb69-b3b641cef6d8 | -7.68344 | -50.26935 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2ea878d-ccd9-39f7-9deb-88fe8b50bc9f | -6.25416 | -43.31384 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 108a9d15-4154-3e2c-a71e-619f0bbd6049 | -5.69736 | -45.15752 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eee187e0-5ab8-3078-a802-5bf0fde50520 | -6.74917 | -58.72537 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c54b16df-d22c-3e4c-8cee-2235f4cab0aa | -9.43953 | -46.79549 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8b6515d-b63e-3b0a-98d4-5f0d7ca8c21d | -6.41322 | -43.26657 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8351cd9e-ceb0-3c50-b006-95c5f86d6a71 | -10.49168 | -46.76604 | 2025-09-04 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| ce1d47ab-be22-3bcf-b5a2-0b4f04cae13d | -6.26692 | -43.5085 | 2025-09-04 04:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 694a1d98-11c3-3d14-a413-06ac40fa9c3a | -5.70276 | -45.15342 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8980402-eb7b-341d-a579-6dd8e4285ef8 | -7.77855 | -50.96515 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c5210b8-ce48-3941-97ba-cace2ea4b155 | -5.69665 | -45.16247 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a44e7c24-abbf-3ee8-85ad-c6fccb8c820a | -9.33044 | -55.2145 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ae6d3f4-831b-3735-b2bf-7401a5cf73d0 | -6.48775 | -44.10295 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35146249-0817-3f8c-a194-a79529f32774 | -9.9637 | -51.63432 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21b9e4b7-2803-36a6-b796-4da0d2cdddb1 | -11.04945 | -45.14767 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 33936cf3-6e07-30f8-9b05-ad26d252c44a | -6.22674 | -43.54021 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90d4f79f-392c-34d8-b242-9e7a1de8c9ec | -10.99343 | -45.91756 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68c420a5-6000-3083-b1d1-672fe50da7c2 | -6.79536 | -44.44894 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c669edb9-c92f-3f7a-8a0b-2ecadc505135 | -8.37897 | -48.32878 | 2025-09-04 04:53:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b88d882e-1d14-3450-8ef1-20529d41f78c | -10.14189 | -46.25333 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e6f6b71-e8f7-3f96-814e-25f940406e33 | -6.127 | -42.94744 | 2025-09-04 04:53:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e5fc85f9-a8f4-3c62-8e56-6c952b9110ed | -6.84228 | -59.15276 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 612ba5a8-c885-3aa9-82e7-a018121d5a04 | -7.25269 | -56.2787 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6bddd7d-b0fb-3e94-854a-fed2237d870b | -6.72579 | -44.15107 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3a932df-4f2b-3f2f-bc15-57be53af1cc6 | -6.22856 | -43.37722 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 22dcc5ae-102d-3f56-98c2-173e14c7e5c9 | -10.52977 | -46.75732 | 2025-09-04 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b5e1415-3d9a-33f1-9a23-563c112eeec5 | -7.77682 | -50.95356 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 734dd6db-28a1-3d22-89ae-cebd5641b13d | -5.39271 | -55.90921 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9c6047e-4577-3ee9-8e96-38dcf9856135 | -8.38045 | -48.31865 | 2025-09-04 04:53:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a883618-7c06-3472-b007-a9295c71007a | -6.86029 | -44.27066 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31dc8a38-4082-3ff5-94a8-1e113479d74e | -8.53213 | -51.32465 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 11f76367-54db-37de-bfb9-ddf4efd087ef | -8.35965 | -48.29475 | 2025-09-04 04:53:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc8da9d5-daf5-377d-a8ff-8bc038e31117 | -7.78026 | -50.95407 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 026361c3-be01-3ae7-8449-b2069e450fff | -6.78568 | -63.13784 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d65bc2e5-ef26-3a41-abfd-2488163a8e0a | -10.22064 | -51.13384 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 434eed7d-94b4-33e3-ba5b-20bba06dfc3b | -9.97849 | -51.62913 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8f2cd51-b970-3323-8154-282fa15ca70b | -6.46901 | -43.9726 | 2025-09-04 04:53:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1508648b-9b9a-3ba0-b022-b93390cb12b7 | -7.70884 | -50.31652 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f09c47d6-e115-34aa-83fe-46261cbe562a | -6.794 | -44.08692 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 70ade86a-c84f-3994-8d54-40d3061b7dc5 | -8.07782 | -45.35352 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e2d22dc-9a09-3b5a-b16b-1d806b70e0d7 | -6.8376 | -46.39611 | 2025-09-04 04:53:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d9f17b6-9842-3897-8451-61d147c96592 | -4.13058 | -54.89733 | 2025-09-04 04:53:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f0b5d10-70dd-3136-846c-a49a86997a54 | -6.68463 | -48.41244 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7ae48540-c074-3b34-b9ef-cb61c02dcc3e | -5.89374 | -45.96025 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8be9bd4-d1d8-3d6e-b0e5-318969ea57a6 | -6.68622 | -48.41533 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d8f5fa93-be26-3285-b582-094345a3f23d | -7.70275 | -50.28454 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0386221e-0439-3037-beca-a99f8ad1fef8 | -3.86697 | -54.60511 | 2025-09-04 04:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57cff901-e9a3-3fc6-a9ca-88cd4735636a | -7.78658 | -50.95869 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a08495c-b480-3439-8144-8723c871a458 | -9.60113 | -47.04716 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 67adbd85-4c4b-343e-8036-b3dd95477911 | -10.21368 | -51.13275 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02bcea2c-45c0-3bb9-9b23-a8b2938c1d4f | -6.23136 | -43.41164 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24e84627-6305-33f7-a08d-af71e995c7f2 | -6.34076 | -53.45324 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c38fec16-cbb6-3e2d-adfc-1cd7169a3cb7 | -11.38963 | -43.56185 | 2025-09-04 04:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 521319b8-8a3d-3a77-9a58-c886481ab79f | -9.61544 | -47.04062 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 900597f3-c6d7-3c1c-971d-2ac89d599606 | -6.67921 | -48.40969 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 94f94e0b-66b5-3a1b-bd50-6ba749cfc9ee | -6.76823 | -63.13453 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2a93165-91fb-3925-8d70-a96c57fcee9e | -6.63198 | -56.2681 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 961611f4-14c8-3cfa-b212-1e203558aecb | -8.02991 | -44.05689 | 2025-09-04 04:53:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c87597d3-a9dc-3119-925e-7e7e6257097f | -9.62416 | -47.84081 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5878a034-2d17-3739-af84-5d46405e6e8b | -6.12815 | -44.14368 | 2025-09-04 04:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac096244-797f-3f7e-892a-3f6be79233c2 | -8.73474 | -47.07669 | 2025-09-04 04:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 177f3188-c6d1-3e7b-a326-a5471e8b9286 | -5.87006 | -46.12463 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a213c27b-a192-31b0-b571-6e9eb2e9536f | -6.49331 | -44.10056 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d9c21ce-be93-39e6-94e2-725e3e788265 | -6.75212 | -58.73442 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8f36272f-16b3-33cf-a5c8-f2f3b6db55a2 | -10.45107 | -50.38626 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c9cc839-a6d7-3922-9906-bd23f0867f73 | -6.87976 | -45.5575 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d2cf04a-d7ce-32c3-aeb5-f70e2c74ef0b | -9.26105 | -56.89938 | 2025-09-04 04:53:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fff7d038-68eb-328e-90a8-6453d7ba23a4 | -11.04473 | -45.14407 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8070e091-5727-34dc-ae51-644d31a041c4 | -10.97926 | -46.83946 | 2025-09-04 04:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f51570c8-7937-37e5-8921-0b14dad77394 | -7.7683 | -45.44033 | 2025-09-04 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d51de77-fcde-3b60-9c25-0fc5ccd96eaf | -5.38706 | -45.94395 | 2025-09-04 04:53:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 501f4b09-84c2-31aa-a892-cb98b7059ba1 | -8.87232 | -45.85808 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1da8e430-b8b1-3964-8d53-eb0c356478b5 | -8.18915 | -49.587 | 2025-09-04 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 200bc01f-61ed-3ab2-ab49-076f34a14f14 | -9.49259 | -47.6162 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cdfd121-d534-35fe-85c4-0ca6da7bfc4f | -10.98379 | -46.84018 | 2025-09-04 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7c2cfdea-9f75-3797-ab59-09f0545adc9d | -7.71297 | -50.28894 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70e5f476-42c7-337d-b58a-05f80c9e0ef1 | -6.77329 | -63.13977 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README65.md)
