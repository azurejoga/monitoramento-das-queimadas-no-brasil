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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbfc58e1-2d67-34dd-8a56-74ebc5dd8848 | -8.16904 | -46.78104 | 2025-09-15 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 457f7669-4504-33bf-a0ca-2b2ffcc8b5a4 | -8.60231 | -46.35106 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1d61eaad-064b-35c2-b5fb-b1d2df4d43b7 | -6.27147 | -42.39365 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4325a2e9-b2ff-35a5-ab65-3200f9ceea6d | -6.40792 | -46.93727 | 2025-09-15 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4ce2462e-2237-3913-9457-6ae7438bcede | -8.20286 | -43.76208 | 2025-09-15 04:19:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 59197095-9576-3b21-98a2-be727c3b564f | -1.95446 | -48.11581 | 2025-09-15 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ea07655-5e7e-3fd2-9f82-174d429e5c9d | -6.97309 | -44.55156 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3448a0f1-ff92-3406-8c2f-65f369eb940e | -7.88683 | -43.58095 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| aeaabecd-cc31-383e-ad6a-0f59c82e8ea4 | -8.40085 | -47.26059 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c96c665f-fe8b-35c9-a48c-eeeb789a9186 | -8.98708 | -45.81291 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a700e7ff-0a70-30ba-a134-2d3ddf2cae67 | -7.88173 | -43.56901 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| ff838787-305b-3262-8574-13d8d70d6aac | -5.74718 | -43.92227 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e62d53f-a981-3d48-a5a7-4bb8a243c25b | -7.057 | -44.14078 | 2025-09-15 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a612b19a-0b98-3d52-8927-cb0db23aa3d8 | -6.45478 | -43.21456 | 2025-09-15 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a513fb6b-b776-386f-af0d-8e678135cde2 | -6.21624 | -46.28815 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2ac7ad7-5947-3846-bff5-860b6c3d7e5b | -5.93414 | -44.86432 | 2025-09-15 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48cbe040-b3b1-3f3f-9334-bbac9e5a0fd6 | -7.10684 | -46.52561 | 2025-09-15 04:19:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8fcf3df-5a11-37ea-9d6e-1ea2ffd70bf3 | -8.62672 | -46.36948 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 17ceb7a8-276e-3542-ba21-b9e03fca02e2 | -9.07015 | -44.82238 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 541e9855-8450-3f6a-bcbb-3e07e17d73dd | -7.68048 | -44.48509 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b238e6bd-f9cc-3a7b-96ee-c914de1be31e | -8.11585 | -50.1689 | 2025-09-15 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8b0ef9a-9187-3b40-998e-603be91aa4a5 | -9.05082 | -45.70893 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f6d7adf-37fc-399b-9b89-226e9a55548b | -6.55293 | -43.99107 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39e5b299-636d-34a7-91d6-c6ebbf4e9ec0 | -6.2894 | -42.39264 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5e8a5af8-b85e-30a2-99b5-f59c9ee5e92b | -5.98469 | -43.77343 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31d5c026-6ed9-34ac-b4ef-30255efd509d | -6.32686 | -43.31733 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| faa37443-b1f2-31c4-bbc2-4a37116dba31 | -8.42196 | -44.96908 | 2025-09-15 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a29ecb6d-a531-33e0-a4f2-d254efb38b20 | -4.15091 | -43.88566 | 2025-09-15 04:19:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 550039e4-0f6d-378b-aad6-47af71af1a1c | -6.94061 | -44.40807 | 2025-09-15 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f06ce01-b3e8-3d03-be14-3df3931b09df | -8.96065 | -45.78728 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 648ece9e-c19c-307e-9ec1-8e2275ee8ee5 | -7.22696 | -43.85395 | 2025-09-15 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4432fa74-55ae-32f3-8176-932f5a34d576 | -7.8862 | -43.56226 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 69e5b096-3bff-3b47-b466-3147f446eb85 | -8.63862 | -45.69282 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 622b1bce-b980-3ae9-80fd-375ff528eb39 | -6.8419 | -45.62564 | 2025-09-15 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13a2c4d0-7c5d-3c68-b682-7e79f8f09ef1 | -5.84957 | -44.1625 | 2025-09-15 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b7aa13d8-04de-3df4-9512-cb57f5b93247 | -5.12114 | -46.13023 | 2025-09-15 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7e2c6a91-12d8-36a1-9a0a-9f404fd2099c | -9.16943 | -45.58195 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8b3390b-c95c-35b4-9306-4664bb09703d | -4.18377 | -48.57152 | 2025-09-15 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5aa0171f-7f74-3058-a9cf-fdcdee376713 | -8.05567 | -44.52304 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 050e7bd9-0bde-365a-b210-1fe43cce9b31 | -7.88228 | -43.56538 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| e4c98f6e-365c-3752-b1a9-27dca9150ce4 | -7.87105 | -43.57108 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dd69f56f-45eb-30bd-868e-520c919cd1af | -7.40064 | -49.99173 | 2025-09-15 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25330c03-86ed-3e93-b400-fc004303476f | -7.8778 | -43.57212 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 3daea202-85a1-3193-910e-1fd09e3ec67a | -7.15658 | -44.33184 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed7144ef-e80b-3563-a82b-bd186eef4ea0 | -6.4211 | -42.60661 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d51b2a9d-76ca-320a-9401-c0226601d7a7 | -2.81012 | -48.62496 | 2025-09-15 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 92bc6f49-0808-3c5a-93d0-df19f8a5cc27 | -7.73301 | -45.30605 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3030474d-e02b-30ff-8232-d30a648106a9 | -5.75455 | -43.92027 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 156ff4fc-6309-3401-ac3b-c4ff3dd434ba | -5.97424 | -45.83995 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57d62bff-16ff-31fe-8658-19574a32087c | -6.17985 | -41.18953 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| de7e3dc1-8527-3a83-b1ed-6cad44b66ce7 | -1.96201 | -44.67281 | 2025-09-15 04:19:00 | NOAA-21 | PORTO RICO DO MARANHÃO | MARANHÃO | Brasil | 2109056 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95681d2b-eb8b-3637-8953-767022cd3670 | -6.05871 | -43.5575 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ed15e3d-f0cc-37c0-90c6-4bfca2eb15f4 | -8.6243 | -45.74048 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3697a5b4-a737-38fa-98b7-acce93831453 | -6.92104 | -46.17576 | 2025-09-15 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b1f5d3bb-d78f-3d35-b383-648626a8d566 | -6.70458 | -44.13235 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5cc7b8e8-bc5a-3c09-a636-e0fe2208a8e6 | -6.56065 | -43.98513 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99526fcd-2368-3761-afc4-8368d583c76c | -8.2006 | -45.57586 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3da3466d-5e41-3e88-b3ad-d81147dd073a | -6.63472 | -44.73511 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9df07583-ddba-3a8d-bf81-1bad5537edc0 | -7.64066 | -49.74234 | 2025-09-15 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 14313f1a-400d-33a7-815f-39d8a7cbef52 | -7.80196 | -46.11744 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 544b5c3b-a562-348a-a847-37d46b5d96b6 | -7.64322 | -49.72738 | 2025-09-15 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58ce6610-d78b-308c-aaa4-36d7d510b4d7 | -6.44487 | -43.32428 | 2025-09-15 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02614cde-6dec-3d89-b579-0fe14b6cb6bb | -5.75401 | -43.92375 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0bfb7b69-87df-3373-9bd1-c0d2defee992 | -7.72532 | -45.31193 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 004d6021-56d8-37e3-9a10-7ea387a9762f | -4.86107 | -45.73302 | 2025-09-15 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29db1779-a594-3b85-a89c-9506c8781de2 | -7.99401 | -44.82983 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59582662-b77b-36bb-a51e-4a95e8a25223 | -7.85633 | -46.11885 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d9a40086-17fe-3cb9-aba8-618e70eae7e9 | -5.11718 | -46.13333 | 2025-09-15 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f2b84f8-02b7-3e7f-96e1-debdf3795664 | -6.21995 | -44.14243 | 2025-09-15 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d64509a-848b-3450-82f4-ea8124618193 | -8.11129 | -50.15981 | 2025-09-15 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e1d18bb-08b9-38c8-bfb5-7887d2e812b2 | -8.90905 | -45.50872 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e7e8662-a278-3675-bdc9-3fc5fb7a270e | -7.88345 | -43.58043 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 195b6251-b35e-3337-a789-ce9dfd9c8499 | -8.63135 | -46.38102 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45c77519-ea02-3367-a5c8-c2782666ba0f | -8.20114 | -45.57238 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f4f3be1-0a86-3e33-add1-b52fa17fc333 | -7.05422 | -44.13674 | 2025-09-15 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d381ee8c-badc-3ca9-a0d9-fd177cdba85a | -8.59785 | -46.35761 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68b1399c-75d3-384e-99b5-afe4db2943d0 | -8.41315 | -47.22811 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5ff99193-e556-3f08-9f5d-bfce20ecc033 | -7.44385 | -45.84377 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 632bab35-4b6a-3824-96a1-d1b577d6c0ca | -8.9156 | -45.48845 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee6aae86-a3bd-31ef-bf82-5b24388f5b78 | -7.8403 | -43.86458 | 2025-09-15 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6575bdae-8486-3bd9-bcdf-4841fd314e3e | -8.62054 | -45.73984 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8b49a44-1ea4-3adb-ae07-29c9b66665e0 | -8.61779 | -45.73583 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bd06b0d-085f-311d-ae49-fb3f3ec1c538 | -8.97222 | -45.82123 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2bff7ddb-2aa6-3807-8eb3-5e4e4db8f7c8 | -7.69047 | -44.68232 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 129cf790-956b-3dd0-86b4-e151e8c7efdf | -7.30637 | -43.95664 | 2025-09-15 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9aa620c-d79e-353f-9044-4357c8552b59 | -6.44053 | -44.08036 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a39bc6f7-72ca-33d3-a3c9-5c11497a0e6f | -9.12576 | -44.83809 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d60b901-cb46-3374-8762-2fe5af245803 | -5.64089 | -45.94721 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 732c981d-36f5-3dbb-b849-3dedfe06f96c | -7.88628 | -43.58458 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 1c177683-865c-3be4-bb26-4b32f8f08133 | -6.81234 | -46.93521 | 2025-09-15 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 547eaddb-6bb0-38e9-8f26-b7c76b9abed3 | -7.59002 | -42.24886 | 2025-09-15 04:19:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1fdc84cc-ca36-3584-98ff-8c6d8d602aa6 | -6.76564 | -44.72435 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6514bb07-1858-36ec-8601-03e8551e4465 | -7.8891 | -43.58873 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 561040ac-4ed4-3765-8384-2e47993a1eb7 | -5.77166 | -43.91937 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbaa5a19-0350-3706-a8a2-5a4d92662276 | -6.43433 | -42.63573 | 2025-09-15 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1b7653cb-fb4f-3df8-8c32-d595c8cc141c | -8.01758 | -44.96533 | 2025-09-15 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3404a9e-7b0d-31a1-ae8f-87d1547df948 | -4.41158 | -47.60759 | 2025-09-15 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 468d3cd7-6b46-368b-812a-fc2c558f3d15 | -8.89698 | -46.1889 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44a4eaaa-d90a-352e-883c-99095728cbef | -4.32779 | -46.73914 | 2025-09-15 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66099046-48ad-30f3-be12-f3efbf373124 | -7.98962 | -44.83625 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README22.md)
