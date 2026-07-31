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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3667ba2c-ff3f-3339-9d69-c3a299f98692 | 1.09753 | -60.52134 | 2026-07-31 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4014fdda-c26c-3ad3-9862-e59cb2d508c6 | 1.10335 | -60.51432 | 2026-07-31 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4aeaeed0-5582-3117-9f32-f0dee2b1bae3 | -4.91078 | -43.46881 | 2026-07-31 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 93a247fc-240c-3b1b-866b-1180e9d49209 | -3.11789 | -47.90732 | 2026-07-31 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0fe4a650-3f38-3dcd-ab3f-df1b726453de | 1.094 | -60.49781 | 2026-07-31 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46a3fc07-5fd1-34b3-ac43-3f547c63e62f | -3.32212 | -48.82184 | 2026-07-31 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31a9a9eb-106c-3a87-8f8b-b173d2fff1fa | -3.61149 | -41.15304 | 2026-07-31 04:38:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 21a70bb7-9999-3698-bbde-b08001ce5e90 | 1.10696 | -60.51471 | 2026-07-31 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 59048007-d15c-37cf-b55c-05b3c9962b94 | -3.05558 | -48.74479 | 2026-07-31 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 03581dff-2672-37d8-9c29-6173002dc78a | -2.7887 | -49.5803 | 2026-07-31 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 680c6045-69b4-3533-a612-0144147e4e97 | -3.99896 | -43.28522 | 2026-07-31 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a3c7bcd-48f9-3e67-b819-06eaea0f4869 | -1.58936 | -50.43618 | 2026-07-31 04:38:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d2bf00e-7fe1-3d8b-907b-8370e5f0c71d | -4.0117 | -48.06384 | 2026-07-31 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e8e94f8-a476-3dbe-9551-af439a764f81 | -3.04898 | -48.74377 | 2026-07-31 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 518326cc-89ef-3f96-a3fb-8966fe272471 | -5.75301 | -43.26727 | 2026-07-31 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a389653-b2db-3948-a239-9c0c2c53a5d9 | -3.99533 | -43.28073 | 2026-07-31 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c59599e-7586-3351-a7d1-94e1deb5b727 | -4.27383 | -48.19394 | 2026-07-31 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f83f9034-7b53-353b-a68b-0c7414536d15 | -3.1107 | -47.90978 | 2026-07-31 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4fe70661-bc61-32b5-8962-6b2ae13a1c7c | 1.10025 | -60.5157 | 2026-07-31 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8530f0d9-031a-369c-b580-766ae0506c54 | -4.91554 | -43.46558 | 2026-07-31 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 33813101-c7fd-3f9c-90d7-e84514827365 | -5.04805 | -43.2659 | 2026-07-31 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45817a56-dee8-39a2-8e4f-9e022e2bf44f | -2.89429 | -48.01089 | 2026-07-31 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c5fb6d93-213d-34b0-b0f0-1beaaa1307fd | -3.61039 | -41.15491 | 2026-07-31 04:38:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 30d59903-2458-37d3-a7c4-434c2d991028 | -3.49661 | -43.31092 | 2026-07-31 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a14dc55c-b312-3868-9c44-ffde3e75640c | -3.96775 | -48.12851 | 2026-07-31 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 53d29fd2-a553-305f-990b-68c155d19615 | -3.70936 | -51.17607 | 2026-07-31 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44db1b75-c141-3a1e-b11b-2c3c0e64da86 | -3.11735 | -47.91081 | 2026-07-31 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 79a1d512-46c2-35f1-9dea-c380fb91dca3 | -3.1168 | -47.91429 | 2026-07-31 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 16994deb-42a0-3d6d-b6a3-4b6a67e1da78 | 1.09576 | -60.50952 | 2026-07-31 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5a078e5b-170e-32e0-8250-e674588bd334 | -2.32951 | -47.20241 | 2026-07-31 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0af49fb6-d413-33db-aa85-e07c4e083b08 | -2.3256 | -47.20545 | 2026-07-31 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29a3e531-4502-3eec-9dd2-da116a7f9db1 | -3.76845 | -49.12463 | 2026-07-31 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcf1104d-59f4-3779-9c6f-da6263c9f745 | -4.38589 | -46.22741 | 2026-07-31 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8bda70c-07f4-323d-bd3b-42f0205e2716 | -4.3669 | -47.76566 | 2026-07-31 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0ef1716c-a423-3282-a5cd-28a681980867 | -5.04378 | -43.26525 | 2026-07-31 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5e1c002b-3ed0-303c-a609-e97c3a18027c | -4.64921 | -43.12598 | 2026-07-31 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df439888-653d-3825-bce7-1b47be0bc0e6 | -2.78815 | -49.58379 | 2026-07-31 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 508728c1-900f-3cb3-9f27-81257fd453c0 | -2.89375 | -48.01435 | 2026-07-31 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 30b018d3-7ec6-3df8-85ff-849241b3f4ff | -3.04951 | -48.74034 | 2026-07-31 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a5dbcb8-23a7-35fc-a0c5-f05def89c1e2 | -2.88989 | -48.01731 | 2026-07-31 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f16f709c-0c6a-3ada-bd50-cfbc54beff40 | -2.91026 | -40.39313 | 2026-07-31 04:38:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ba47c140-44e4-3e2f-a3d4-dba4259571c2 | -2.32615 | -47.2019 | 2026-07-31 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 253bb4c3-2bd5-3297-af66-90678dfcba27 | -4.93983 | -41.98541 | 2026-07-31 04:38:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e3037d19-9bb5-3adf-8b82-afc55f95a3df | -3.96829 | -48.12502 | 2026-07-31 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7e7db61f-efad-3ca0-8c7b-751735aa09bc | 1.09749 | -60.49813 | 2026-07-31 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9133fc62-10c5-3d0b-8455-664143f9a92d | 1.10118 | -60.52158 | 2026-07-31 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7cee0f1b-65ac-32e0-aee2-afc5fab98aff | -3.71283 | -51.17662 | 2026-07-31 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 15b6b566-fa68-37d5-977d-a98b21189873 | -4.00488 | -43.27427 | 2026-07-31 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70c99885-cdb9-3c0a-8bc7-4ccbd26c4396 | -3.99953 | -43.28137 | 2026-07-31 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6dee074c-190c-36ff-aaf6-8fafe11d46ea | -3.7149 | -51.1772 | 2026-07-31 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96db9629-f7a8-3a08-97c0-bc608678c615 | -2.82568 | -49.49675 | 2026-07-31 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d4545f7-b475-3651-889e-781bf7eddf62 | -3.32158 | -48.82528 | 2026-07-31 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59ba7241-31f2-32e6-ba9e-393c4ec79025 | -4.27715 | -48.19445 | 2026-07-31 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a6a406cd-a4b9-39c7-9f82-b64963039754 | -3.11348 | -47.91378 | 2026-07-31 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 80f7c0e0-4cc1-3ab5-b2d3-3a6f21a0b3cb | -2.47312 | -54.7101 | 2026-07-31 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a67c6324-173a-3b2d-80ef-ce6c95f753ca | -2.49042 | -47.08857 | 2026-07-31 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b85a9073-0286-3931-8fab-1de4efbadd0a | -3.05228 | -48.74428 | 2026-07-31 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b4a703b2-61a3-3b7d-bcf8-2b437cf8f3b2 | -4.3697 | -47.76972 | 2026-07-31 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1e097fb7-5662-33ec-a83a-e56a8f963c70 | -4.27329 | -48.19742 | 2026-07-31 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 55dd60e2-e03c-34dc-b37c-df641e3cc62d | 1.09933 | -60.50982 | 2026-07-31 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7586ff21-89d2-3f20-a151-d9918cc5f8d5 | -4.37305 | -47.77024 | 2026-07-31 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dde9c846-22ce-3d87-b600-8df319ddc328 | -14.3855 | -48.071 | 2026-07-31 04:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| d74ba481-0e8c-3947-a0dc-22b554b5c03b | -6.12673 | -43.75714 | 2026-07-31 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 030904b5-a497-3dd6-9c19-89f7ee4f333c | -11.93528 | -43.43977 | 2026-07-31 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3668c18a-d813-3233-942d-72ecf0cda881 | -12.61024 | -44.60264 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a15378c-fee9-3b78-95dd-88ff8235d101 | -9.70223 | -47.31395 | 2026-07-31 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25a57d68-0e28-31cc-8888-66b19edcbe4c | -6.10541 | -49.38673 | 2026-07-31 04:40:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d07b83eb-f428-3ed8-b080-5ec7cf9f7840 | -10.63502 | -47.48544 | 2026-07-31 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 935b49ad-ec36-3768-a921-aa0e161e89b2 | -11.75576 | -46.73657 | 2026-07-31 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4759a80-a067-3d9b-ba3c-055cf61b2017 | -7.00603 | -47.97947 | 2026-07-31 04:40:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fe29c63-1549-3db4-b6f3-41ddd1619d68 | -11.44844 | -50.10099 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 769a3c68-f41a-3530-9b70-a686ff8b0a6d | -10.84674 | -44.55711 | 2026-07-31 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bdc0c07-d5fa-3ab5-8b93-bd414abf64ee | -5.71933 | -48.12141 | 2026-07-31 04:40:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc5d7625-0794-3636-bf61-d8691904455d | -12.85185 | -44.39302 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ed775c3c-3c99-3eed-ba99-44b706eb77ba | -6.56824 | -55.14308 | 2026-07-31 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fdad7c9-50d4-3aee-8bc4-0c8363872c79 | -12.59826 | -44.61632 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07bda653-3c54-36e2-bb01-c7b39186c94a | -5.71697 | -47.2579 | 2026-07-31 04:40:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98a79032-502d-3d3c-87d2-c23b6e3d2557 | -10.90339 | -45.20461 | 2026-07-31 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60163723-8f2a-390a-b864-63b2f87ab516 | -5.81056 | -43.64177 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d965537-911d-3dd2-91ef-236acc29e58a | -8.9995 | -45.18155 | 2026-07-31 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c90f6dcd-7812-3d6d-a966-fdac7d70bf33 | -12.60591 | -44.63659 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d82a2bb3-5dcd-34bb-ad26-74f08e1d90bb | -5.63542 | -47.10419 | 2026-07-31 04:40:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26f36470-acbe-3f28-b580-10dd7ee4158e | -11.30629 | -50.2945 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8b0a890-7cfd-3f32-bd0e-81ce8b4081a1 | -12.60902 | -44.63509 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37ea5fd5-1733-37ba-9e44-1c2a0e8b4e0c | -9.08322 | -46.06536 | 2026-07-31 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb3dc223-545e-3f22-a827-be0706840642 | -6.35432 | -43.2836 | 2026-07-31 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e6fa361-4fef-3578-a8c4-11d2032f7222 | -9.56229 | -47.11469 | 2026-07-31 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2883c7b-69a2-38f5-9c19-039114a05822 | -12.60868 | -44.60484 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c26c4dda-45f8-35a5-a853-ff3175b10163 | -9.08386 | -46.06084 | 2026-07-31 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bb46445-b247-3e6a-a85c-a45068147169 | -12.34322 | -48.21964 | 2026-07-31 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f474053-08b6-30c6-95f9-57ebe9791bf5 | -12.59279 | -44.6241 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f488e5ee-51af-3a19-95f4-61b2b7f3bed2 | -7.04058 | -46.51009 | 2026-07-31 04:40:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55a1fef8-d4f6-3d65-a47c-8d21f2b962ea | -6.97725 | -42.88231 | 2026-07-31 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a981fe3e-d28d-332c-9483-10d90c666fbd | -7.61694 | -45.18544 | 2026-07-31 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 899df504-c842-34cc-be87-0b01bfd9af12 | -8.22197 | -42.58775 | 2026-07-31 04:40:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f44eb6c-2b08-373c-b1b8-901563b4299e | -12.6229 | -44.5981 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a36f278-4a2d-3ea9-b089-eea462e67073 | -11.74134 | -48.91036 | 2026-07-31 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 937af333-a23d-3579-84a7-30e4daaabb0e | -12.62441 | -44.59589 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 742f4bc7-03a0-3165-85f7-80a1917b14dd | -9.17514 | -49.67622 | 2026-07-31 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a4b8a81-aa98-37cb-8a03-d88138889527 | -11.4617 | -50.10308 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README8.md)
