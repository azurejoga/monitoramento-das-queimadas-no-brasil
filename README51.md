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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2b1a05a-ddcf-3f88-b8f6-ec145dcc9406 | -17.91535 | -43.43884 | 2024-10-04 03:17:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 050103ac-544c-3a0c-af79-70854bf7043a | -17.91477 | -43.43785 | 2024-10-04 03:17:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dc3c1550-0c0a-37b4-a67a-d9e3b165a8e3 | -17.91441 | -43.4431 | 2024-10-04 03:17:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9e4b52a9-eaf2-3f67-bacb-872d09900d92 | -17.9138 | -43.44214 | 2024-10-04 03:17:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c587d28c-920f-32b8-84e2-da2ef1614c15 | -17.91348 | -43.44731 | 2024-10-04 03:17:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb9c7d00-1180-3835-ad69-deeb6c2d1f8f | -17.91284 | -43.44634 | 2024-10-04 03:17:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 25f21914-baa8-3036-aaaf-6e577147f2dc | -17.91254 | -43.45158 | 2024-10-04 03:17:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4381cb66-ca1a-3e19-9b38-78b54560ae63 | -17.91187 | -43.45061 | 2024-10-04 03:17:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e751f7d-d723-393a-a839-085b44e2fb1c | -17.74319 | -43.81689 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b9814c50-e2d0-39e2-82da-419da26bc2a7 | -17.74184 | -43.82306 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 601db1c2-fa6a-3b12-9887-1aa89316fe09 | -17.74051 | -43.81337 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 7188db01-f0fb-3fd5-bb92-2f8e3aa56d27 | -17.73907 | -43.81968 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 21.1 |
| eaabf2ea-4345-3706-81f2-d551adb29411 | -17.73824 | -43.80948 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c3e730f6-2824-3fe7-935f-b9a5b821ae1b | -17.73774 | -43.82558 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 1cfb7aa4-401b-3c2c-9e42-e6da45fbfe42 | -17.73693 | -43.81544 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a13c39b7-bbbc-3873-b9ea-c79c169c40f5 | -17.73559 | -43.82153 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ccdfa508-6e5a-3026-9261-20784373cacf | -17.73558 | -43.80606 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 635b54a4-2dd4-3003-8f74-08f42fe3bfc8 | -17.73432 | -43.81161 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f1e3c9cb-f5f8-35f0-b3cf-10734932b3c5 | -17.73295 | -43.81764 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| bc2ada69-e4a4-3722-96ef-1f8a87b82a38 | -17.7321 | -43.80747 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb212113-0d20-3856-a9bc-82510fdf8988 | -17.73086 | -43.81311 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef7eafbf-c464-3850-b3a4-0f8231b61e2a | -17.6922 | -43.77978 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1017cd0b-83a1-386d-9d77-0cab8e2ed4af | -17.69098 | -43.7852 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d32fbb54-b199-34d7-9426-459532565b1f | -17.24309 | -43.188 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5eb8b08-471b-3ee2-8575-ecc0f7955923 | -17.24272 | -43.21853 | 2024-10-04 03:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07635aea-e31a-3d15-9a26-db693c081783 | -19.28212 | -43.78009 | 2024-10-04 03:17:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 878bfa2a-18cb-3569-9dab-d3cc73f3f3f4 | -19.28148 | -43.78316 | 2024-10-04 03:17:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 14e0b301-960f-3d85-828a-19a93158e3de | -19.28107 | -43.78485 | 2024-10-04 03:17:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd9c6904-9c1f-30a1-bcd4-03f74beabca0 | -19.28001 | -43.78962 | 2024-10-04 03:17:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b73a9d2-c33f-3de0-bdc9-9730ae286eab | -19.27929 | -43.79272 | 2024-10-04 03:17:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 277bba5b-7888-3e3c-895a-d2a6e957944d | -19.27825 | -43.76876 | 2024-10-04 03:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38c90114-9b76-3908-a639-e992d756377c | -19.27761 | -43.77214 | 2024-10-04 03:17:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a0961317-cc32-3de5-aed2-e295ab08f6c4 | -19.27712 | -43.77383 | 2024-10-04 03:17:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0aae79af-d9f1-30d3-8ca8-6593fe7b57e0 | -19.24984 | -43.37841 | 2024-10-04 03:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fdc07eb-370c-3f08-9f76-1345ed93db25 | -19.24885 | -43.3829 | 2024-10-04 03:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5acff2f0-3f22-3f37-b06e-dd5e0f40c8a0 | -19.24781 | -43.38761 | 2024-10-04 03:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17783321-235b-3911-8611-5740b062cd9c | -19.24198 | -43.36853 | 2024-10-04 03:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f30ce7d7-f8a4-3d06-a218-77e072befe89 | -19.23906 | -43.37069 | 2024-10-04 03:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 75f447b6-64ee-30a5-aa5e-8bf6fdce834a | -19.23718 | -43.37915 | 2024-10-04 03:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7f5c2232-3e6c-35e4-9cf7-ecd5fb64ba9d | -19.23598 | -43.3846 | 2024-10-04 03:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce6cae76-74ce-39d9-9b28-6453468881cf | -19.23586 | -43.36799 | 2024-10-04 03:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2e8d0c23-084a-3b8e-9382-e09b3d43e42e | -19.23487 | -43.37233 | 2024-10-04 03:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 511f469d-b0b4-3450-87d5-73c63f54a8fe | -19.23389 | -43.37659 | 2024-10-04 03:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c1286ecf-b7c3-316f-8df2-00bd0a588b65 | -19.23285 | -43.38116 | 2024-10-04 03:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43918811-9312-353b-85f7-af79e67f4136 | -19.23182 | -43.38567 | 2024-10-04 03:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddfc9de4-b8d6-3939-af2e-51f321e1388d | -19.22998 | -43.38349 | 2024-10-04 03:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52a5fc52-6538-36d4-b355-86bdd4e4002e | -19.06018 | -44.44373 | 2024-10-04 03:17:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5bc1b396-2c36-3b79-9f08-1ddfd5b95188 | -19.05894 | -44.44912 | 2024-10-04 03:17:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17d8294e-1df8-36e6-972f-7fc23e314880 | -18.98448 | -43.2854 | 2024-10-04 03:17:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1ee5479b-60eb-3ec1-92dc-4dc31f278f0e | -18.8795 | -43.46571 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 885466fc-2805-3f5d-a3d4-19224f9e2d43 | -18.86293 | -43.59924 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 6c87807f-cd5d-379e-97c7-02d236e71fb7 | -18.86283 | -43.57185 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5ff4a13e-3101-3bd7-9fb5-edf229a3bfc6 | -18.86221 | -43.60075 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| d2dca512-410d-3eb9-9c3a-9544783de5d5 | -18.86202 | -43.57293 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c0722c80-7ab9-39a1-966b-39432e010fab | -18.86201 | -43.57543 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bed58f87-3eea-3359-97f4-bdca0c6a1e2b | -18.86122 | -43.57655 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3a47dcbe-7a43-346b-8a0e-e6c9069de02f | -18.85821 | -43.59201 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1b31debc-b072-3415-a172-dc151c343cb2 | -18.85749 | -43.59331 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| dfbcc160-ed22-3b6d-93e5-6a8735205be5 | -18.85715 | -43.59663 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 9832aaa6-5f7a-3900-ba8d-aa3242ae3562 | -18.85655 | -43.569 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0f6de312-41b8-3631-9f4b-998270c08e29 | -18.85649 | -43.57172 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b24833e3-5e50-311d-90f9-227a5bada95d | -18.85642 | -43.59808 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| cc49f60e-a891-39ef-8e33-0d4d151d196a | -18.85598 | -43.60175 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 86260d65-2bee-3475-8833-93cdcbd39b5d | -18.85567 | -43.57292 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e9f45081-17f4-37a2-a2a4-9e31a040aaa2 | -18.85528 | -43.60323 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| cd922e18-8b40-31f4-a721-197446dccc5e | -18.85483 | -43.57669 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2c3f2b93-3bdf-3d6d-8d45-77adef27d59e | -18.85458 | -43.60783 | 2024-10-04 03:17:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 042a3935-050e-30ff-9ee1-85c391378a19 | -18.85398 | -43.58047 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d9c09d3a-ad63-3c6c-9bfe-a79af5e29dbf | -18.85388 | -43.58309 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| cc1c5804-fea7-34e1-a8dd-998bcf1e0875 | -18.85381 | -43.60988 | 2024-10-04 03:17:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 325e4dc2-84bb-33d0-b8b7-7de871f9df85 | -18.34537 | -44.01686 | 2024-10-04 03:17:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 39edc5d8-2354-38a8-bf1d-7ced6f19eb48 | -18.85314 | -43.58427 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0252b583-1502-3cc1-b4ce-6c812ce9a40f | -18.85299 | -43.58694 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b1c75642-02f7-36d5-a7cf-2c80941623dc | -18.85298 | -43.6148 | 2024-10-04 03:17:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 815da11d-3e0f-3655-98c5-cfd8d5b4de72 | -18.85228 | -43.61679 | 2024-10-04 03:17:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 2010f66f-6a6e-3438-9198-9ac88357b265 | -18.85226 | -43.58817 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 35f2cb87-8bc0-3323-88a2-735fc79e690d | -18.85205 | -43.59105 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| fb5d9f13-4e8b-3970-b90e-29c5109def06 | -18.85133 | -43.59235 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 63787bb9-9a6d-3bd0-8326-ed6436fdc0a0 | -18.85106 | -43.59534 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| dcf156f9-2354-3fc3-a1ce-cb7207bb6a12 | -18.85035 | -43.59675 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 85f21f3b-389c-3eb5-b21f-80fe48513aa1 | -18.84994 | -43.60025 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| bdee4cf9-0d17-39b0-a722-9e6383044313 | -18.84928 | -43.57306 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 42238687-9120-35b4-951a-6dfd08d9c944 | -18.84923 | -43.60179 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| c6914189-6e0b-36ba-a55d-4b1ffad1203c | -18.84843 | -43.57685 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d9653d45-c349-3fc5-8a47-2c86bf7c578c | -18.8476 | -43.58057 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3cffd196-00e9-343d-b80c-ade072ee63d4 | -18.84679 | -43.58418 | 2024-10-04 03:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 875f5369-2684-3f6f-b2a4-aaba609674d9 | -18.58716 | -43.96711 | 2024-10-04 03:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73201a9d-2471-34db-9ce1-947423e8215e | -18.58441 | -43.96207 | 2024-10-04 03:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 622e4de7-5941-38f2-8eb6-9a969e7c5339 | -18.58286 | -43.96909 | 2024-10-04 03:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fcbee1d-9c06-3892-b379-4c54108668c4 | -18.58263 | -43.95828 | 2024-10-04 03:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31901049-7df7-353c-a4d0-c2f7d5f728e1 | -18.58133 | -43.97599 | 2024-10-04 03:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 303802e9-5f9c-3620-8898-e1a5e813f174 | -18.58106 | -43.96515 | 2024-10-04 03:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0abe3d0b-3dc4-333a-b852-290035c13011 | -18.5795 | -43.97195 | 2024-10-04 03:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 628fcc8e-75a5-3a58-81da-2a85dc198624 | -18.56548 | -43.84246 | 2024-10-04 03:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bc58072-f2dc-3e46-8dae-d90e58fa820b | -18.56442 | -43.84719 | 2024-10-04 03:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e83dfe1-d3bf-30d8-8648-17b2fc357937 | -18.55943 | -43.84045 | 2024-10-04 03:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 994919ec-65b8-3624-b6ad-329143656599 | -18.48856 | -43.87656 | 2024-10-04 03:17:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efc6a9ee-f9db-3afd-8a2b-0fa0ce46dd2f | -18.34868 | -44.01777 | 2024-10-04 03:17:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| db33d684-40cd-3340-a579-64f08fbafed9 | -18.34713 | -44.02476 | 2024-10-04 03:17:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4637f32f-546b-3d32-a0e7-c9cc976bc9c2 | -18.34386 | -44.02342 | 2024-10-04 03:17:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |


[Clique aqui para ver as próximas entradas](README52.md)
