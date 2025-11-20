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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40ff7968-6b78-3562-a25f-19be480af776 | -20.24877 | -49.33587 | 2025-11-20 04:36:00 | NOAA-20 | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3db9b058-51e5-3fab-9a22-9f689bda1f19 | -17.61831 | -54.18702 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f43c1532-76cb-377d-b837-7af0064bdaba | -20.29239 | -50.97568 | 2025-11-20 04:36:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.8 |
| 751bf068-0b2d-39cd-bfd2-ff86f72a3a36 | -19.83336 | -46.93082 | 2025-11-20 04:36:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46895770-c46b-328c-a21e-3949f7d23837 | -17.53618 | -53.71378 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e802a93f-c0e6-3029-b90f-73d2b99184f6 | -16.31102 | -53.82367 | 2025-11-20 04:36:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c3496e9-6be0-32db-ad98-b51bb57b6f09 | -19.47593 | -53.94434 | 2025-11-20 04:36:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50630857-e126-3dad-8335-fba71a051ed2 | -17.61543 | -54.18185 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 345ee53c-a30b-39fd-91a2-601280bb6916 | -20.20555 | -50.74971 | 2025-11-20 04:36:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a55435de-be87-38c8-b2d7-0b25ae5d626b | -17.5305 | -53.70379 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91e71f59-3e4e-3550-a54c-0f806ca73cce | -17.46944 | -45.7503 | 2025-11-20 04:36:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cfd4361-209d-3917-bb75-62bfe125bfeb | -17.62199 | -54.18765 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 52ee0266-b0f5-3b6a-84c1-da5b62c65491 | -17.50539 | -44.9222 | 2025-11-20 04:36:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b059dc34-0178-3a05-a650-fad38a82c8cc | -16.28709 | -52.93199 | 2025-11-20 04:36:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 419e9e7d-a963-3839-9591-5ab6cc591b24 | -17.50367 | -44.92456 | 2025-11-20 04:36:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c3bbc15-36c5-3d54-bd97-a94828dc288b | -21.78218 | -43.43777 | 2025-11-20 04:36:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 11b53928-e9d5-30ce-8c7b-6c649214747f | -18.12179 | -54.52623 | 2025-11-20 04:36:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 20480b47-a0c0-36a0-a514-14639ecd5f7b | -17.52975 | -53.70814 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b3f7e1a-3100-3feb-95e5-f71af895d4ba | -20.2885 | -50.97876 | 2025-11-20 04:36:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 04b2e962-96be-36b3-a502-000e871b3dad | -18.15846 | -54.55754 | 2025-11-20 04:36:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 75105627-a89e-339d-84b8-a75c137ddb4f | -19.47444 | -53.953 | 2025-11-20 04:36:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4ba73efc-c3dc-376d-bc13-33b3e2783141 | -19.56287 | -49.49952 | 2025-11-20 04:36:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 60bc7746-572e-395d-a562-34b4c22e3c60 | -21.24762 | -49.16798 | 2025-11-20 04:36:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0b3a6392-8400-3d5d-8888-e4cb728d39a9 | -15.54451 | -50.66535 | 2025-11-20 04:36:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cdd4d3df-538a-30a1-b9af-9eb56e90970b | -17.90356 | -49.36732 | 2025-11-20 04:36:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74be17a5-0e44-3424-bdc8-d78118b32cb8 | -16.29741 | -52.93643 | 2025-11-20 04:36:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 303c3bb9-843f-3290-bac3-52cf047d7bfc | -20.29742 | -50.96526 | 2025-11-20 04:36:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 50ff3c4c-0019-30ca-b59e-27abe2657063 | -19.77068 | -48.01185 | 2025-11-20 04:36:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a54c28c7-93e8-33eb-8e87-b0ad01b21e94 | -21.03892 | -48.55018 | 2025-11-20 04:36:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 5e5aebfb-2fd6-3e28-a50d-664582834402 | -16.47737 | -52.48996 | 2025-11-20 04:36:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c63d96b4-54df-3350-af33-0832f7e5ad9f | -21.16363 | -48.63768 | 2025-11-20 04:36:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2f31a7f0-07cb-39a8-908b-d6c20db72d87 | -21.03833 | -48.55438 | 2025-11-20 04:36:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| df597440-56cf-3ccc-aebe-546a90205464 | -18.50525 | -50.74363 | 2025-11-20 04:36:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76db0b1a-e8c7-3072-975d-b323241cb874 | -16.87144 | -52.65223 | 2025-11-20 04:36:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df852a04-090d-340c-879f-15022613012d | -17.90335 | -46.71533 | 2025-11-20 04:36:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| def16e3b-eacd-3e3c-a1a4-7630693d3611 | -15.5412 | -50.66478 | 2025-11-20 04:36:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 429aa86b-24f5-3251-ae2f-500fb1edbe48 | -20.29296 | -50.97202 | 2025-11-20 04:36:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.8 |
| 46da25f4-5307-31c5-bcfb-d0607c513abb | -15.96159 | -52.21227 | 2025-11-20 04:36:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d04d27a-895c-3516-815a-3dd50c8b5302 | -16.29672 | -52.94044 | 2025-11-20 04:36:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79b6ce1d-5eca-37e7-80a8-33a3bf71671f | -16.45333 | -45.01612 | 2025-11-20 04:36:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b699dd3-13c6-3d39-b74e-f77201727e72 | -17.80255 | -54.69915 | 2025-11-20 04:36:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9242574-ad27-3f6b-83e6-210a04e4641b | -16.29697 | -52.93794 | 2025-11-20 04:36:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c6aeae77-6533-3f67-b688-663587cd0801 | -17.61912 | -54.18246 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cee420e4-a81f-3f30-9a80-f512b8fb5e67 | -21.33284 | -48.69117 | 2025-11-20 04:36:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bd648a5a-b3a4-3567-8007-903610af9475 | -17.50488 | -44.92603 | 2025-11-20 04:36:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c542e69-f778-31ee-b3dd-a8fb2816d283 | -15.54509 | -50.66176 | 2025-11-20 04:36:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24d9db4a-55d5-3b29-be05-e5a33c25ba73 | -17.5341 | -53.70444 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8ae42c89-e5a6-3613-b679-11612175fcb5 | -18.18785 | -47.65376 | 2025-11-20 04:36:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 460868e9-c071-3a95-b335-b0a5e354ab5e | -16.32521 | -50.05001 | 2025-11-20 04:36:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7834fb30-356d-33dd-b948-410ee27f7107 | -20.23745 | -50.67598 | 2025-11-20 04:36:00 | NOAA-20 | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cd9fb5fc-c43c-35d5-8207-0d36f9ba1df8 | -20.88666 | -52.35291 | 2025-11-20 04:36:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77a4fcc6-815d-3cf6-9383-6e5392aada9f | -19.47873 | -53.94936 | 2025-11-20 04:36:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe3d4ce2-b87f-390a-b73a-4c4b170abff0 | -17.53694 | -53.70943 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 72cf7190-9a89-3dfc-83ac-fd646d1030bd | -20.29799 | -50.96159 | 2025-11-20 04:36:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| e884829c-9414-3a40-b527-a9ed1df7f48e | -20.8879 | -52.34537 | 2025-11-20 04:36:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a198b98-0caa-3ef3-9d3c-3fcf3298f8ab | -20.56071 | -49.56829 | 2025-11-20 04:36:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 425eb806-8b78-3591-bf94-a60e3e733564 | -20.88332 | -52.35227 | 2025-11-20 04:36:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b2f5107-8109-3d83-84e5-3c3ad97ad161 | -18.12263 | -54.52153 | 2025-11-20 04:36:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6118df60-3cd0-365d-82d4-846025e355f7 | -17.50437 | -44.92986 | 2025-11-20 04:36:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71ad3cfa-8472-30b2-8c96-41a95b64085a | -17.61993 | -54.17794 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a4f4fe0-e85b-353f-888c-9c6fc8a27bd6 | -20.28908 | -50.9751 | 2025-11-20 04:36:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| e81042af-a755-3717-9486-411acceb6d8d | -20.88394 | -52.3485 | 2025-11-20 04:36:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6c46817-950a-3a2f-bc3f-b9cac9ba2986 | -19.94442 | -46.99265 | 2025-11-20 04:36:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b59ecea-4b78-34d4-9469-1957afe5099d | -17.86147 | -45.23362 | 2025-11-20 04:36:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4af1953d-c58b-3100-94b2-66b269e295ba | -17.53334 | -53.70878 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c07a0761-de4e-371f-8799-5424b16417c1 | -17.53259 | -53.71313 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9151fa9-b705-31ee-af84-82663c744e3e | -17.61462 | -54.18642 | 2025-11-20 04:36:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 025feb27-5d95-346a-879d-d45705d1d524 | -20.30073 | -50.96584 | 2025-11-20 04:36:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| c8d27f78-1ee7-3686-b040-d3625e6e9adc | -21.33343 | -48.687 | 2025-11-20 04:36:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4ce789f0-d672-32f1-99de-8c4ffaea0301 | -21.04186 | -48.5549 | 2025-11-20 04:36:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 08eb3cc6-0b56-3c24-9023-0a1e2b84df5f | -16.20091 | -52.58501 | 2025-11-20 04:36:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08a16519-3bf2-3ea6-894d-6e4db7112779 | -21.24705 | -49.17198 | 2025-11-20 04:36:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4bb192d8-513c-393a-bd8a-9ea242b2ac9e | -19.08043 | -41.75922 | 2025-11-20 04:36:00 | NOAA-20 | CAPITÃO ANDRADE | MINAS GERAIS | Brasil | 3112653 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6132f7e4-d281-3a6d-b368-c74405529c12 | -17.17406 | -43.30199 | 2025-11-20 04:36:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45a278d2-44bf-38fa-91d7-f23032970adf | -20.24134 | -50.67287 | 2025-11-20 04:36:00 | NOAA-20 | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b0cee00a-3b89-3a5e-ba95-a46ece94f68a | -21.05499 | -55.81311 | 2025-11-20 04:38:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bb7b93a-5137-35ff-b2d0-7687d0b579d5 | -25.05655 | -50.17635 | 2025-11-20 04:38:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3bf67f17-f1ea-30da-8322-972d0c98b59c | -25.82681 | -51.24815 | 2025-11-20 04:38:00 | NOAA-20 | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 55506cc4-8a2a-3694-b562-37dfabf18ad0 | -22.42407 | -47.63105 | 2025-11-20 04:38:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| defc764a-e925-3fa5-9f5c-6a0da863f3b8 | -22.42838 | -47.63375 | 2025-11-20 04:38:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 30717b98-5f39-398f-90c3-8019dbec8dc6 | -22.42782 | -47.6316 | 2025-11-20 04:38:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c769ff1d-456a-37d6-9632-ac7a6c09199d | -21.05119 | -55.81228 | 2025-11-20 04:38:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05420c77-e448-34ba-a901-00db420c53fe | -26.43233 | -48.71954 | 2025-11-20 04:38:00 | NOAA-20 | ARAQUARI | SANTA CATARINA | Brasil | 4201307 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2f1f595b-90ba-35d5-9965-c06210f678bc | -22.42463 | -47.6332 | 2025-11-20 04:38:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 33c27268-a7be-365f-af24-fd0d5ae2cb20 | -22.97478 | -48.67175 | 2025-11-20 04:38:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e9e9f5b-9f67-333e-a432-23f229402a2c | -22.83176 | -46.32016 | 2025-11-20 04:38:00 | NOAA-20 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bceba2e0-e1a7-36af-aa21-09227cb4d6c7 | -32.45392 | -53.0453 | 2025-11-20 04:40:00 | NOAA-20 | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 7f7a6cb8-fdbf-3b42-b5a5-752bdaac3a86 | -32.08931 | -52.15556 | 2025-11-20 04:40:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 443cc105-b732-3424-a02d-3be470b1525c | 3.10961 | -60.76741 | 2025-11-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 852acf40-fd34-3a5a-ac6b-e4371b23df80 | 4.38838 | -60.18772 | 2025-11-20 05:20:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5ef5148-f168-3ec8-b611-295992023997 | 3.10613 | -60.76794 | 2025-11-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0b70ebe9-1b4f-33aa-9b72-d780027de197 | 3.10553 | -60.7641 | 2025-11-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 85ab4d73-3208-3a36-b88c-8c0aadfbe836 | 3.10672 | -60.7718 | 2025-11-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1ce9f600-55da-30da-af29-b9245230d208 | 3.11369 | -60.77073 | 2025-11-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c99ae204-411a-34c5-a9de-ab4d1528bc6f | 3.10901 | -60.76355 | 2025-11-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 18.4 |
| c70863f4-56d9-3313-a0b1-0c1696d049a6 | 3.11021 | -60.77127 | 2025-11-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 20914d3d-f9fa-346d-85ee-aa3600e36c16 | 4.39179 | -60.18697 | 2025-11-20 05:20:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60e16e52-5d70-3915-aabe-060652b4413e | -9.71326 | -61.29739 | 2025-11-20 05:22:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0146cde8-0660-3c4a-b9b6-b215b4135c3b | -4.10254 | -50.06451 | 2025-11-20 05:22:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6523a3c5-c03c-3cbc-9fe0-a51376adcdc2 | -9.73204 | -63.64619 | 2025-11-20 05:22:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README14.md)
