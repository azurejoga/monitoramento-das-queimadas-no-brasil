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
| 001c58ba-a7b0-3a9b-a371-b4bea6e545e1 | -11.10064 | -52.02358 | 2025-09-05 04:36:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91e62440-dd5a-3ae6-b436-bb56b67c7dae | -8.01353 | -45.43849 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32604335-123b-3110-9447-2923afc60e33 | -9.37896 | -50.38814 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca61ae51-e799-3420-8ff6-dadd7139fe51 | -7.6186 | -47.93564 | 2025-09-05 04:36:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66a8807f-a299-38db-b3d8-1ca6e97a63ef | -12.97653 | -48.05285 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8e2394b-12a7-3ba6-a6c4-83360e46be1e | -9.98167 | -51.63087 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db48e45f-b2a7-32ce-9da2-304af736a8c9 | -11.65058 | -46.85868 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b8b63ca-548d-3426-aa07-e62e65c25ee1 | -12.97124 | -48.08239 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74f66573-de2c-3b9d-9b01-0dd85395b9f5 | -11.64315 | -54.53638 | 2025-09-05 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b91754ae-f38f-3d7e-905a-645fba8fdbc8 | -9.70224 | -51.0712 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d184109-fdef-3923-90b4-4bfa9c1f5ef6 | -7.61363 | -47.94556 | 2025-09-05 04:36:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43355288-51ec-3657-b76c-5ee94f611eb2 | -8.07891 | -49.90059 | 2025-09-05 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f32d88bf-b6a1-3766-91a5-3b94a5a84144 | -13.74772 | -46.93162 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 060a0b77-f912-341b-ab28-7385b7dcd700 | -13.45778 | -46.92017 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6027ee48-ecf4-3a76-b5bd-8775c37fa0a8 | -9.82192 | -48.30825 | 2025-09-05 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed6ab00f-008a-31e1-9afa-2d69f93d73b5 | -12.18856 | -53.89632 | 2025-09-05 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9eb921e5-8fa5-3d0c-8ff9-6928130e00ad | -10.23138 | -50.53767 | 2025-09-05 04:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35a0e26e-0f87-38a8-924b-0dd60bc17b79 | -8.97607 | -44.45306 | 2025-09-05 04:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebd958e9-f523-3e81-ac24-5648adfd9b6c | -7.6889 | -50.25776 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d6bdb60b-a3dc-31fa-b01f-5f7750dd2a31 | -10.47557 | -53.64336 | 2025-09-05 04:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6722351-b965-3c5f-ab9d-6b6532bd74cd | -11.58442 | -52.10493 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f8c5eb2-b530-32f1-a2fa-297463362c74 | -12.39908 | -54.96003 | 2025-09-05 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7701948b-eac3-3ad2-babb-b7a30f97441c | -11.59026 | -52.17999 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 577660bf-f456-3fb1-9d0a-14b3216506af | -9.07209 | -46.99773 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| de7369d8-8fc8-3b80-86dc-a600ffd69015 | -10.44648 | -53.61406 | 2025-09-05 04:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9ed3bf5-0de7-3a41-9ff6-6fda3cbaa5ca | -11.99511 | -46.74603 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c104d02b-fb3d-37e3-8bd4-c848e1884377 | -11.72523 | -47.75395 | 2025-09-05 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38706562-8745-30f8-bb5d-9b3bbd50c865 | -13.65806 | -47.92424 | 2025-09-05 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65b4817a-4b99-3119-a524-a99bcad762ba | -13.28987 | -46.81649 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebc1ce40-f451-33a1-a422-9b74fd406caf | -12.46929 | -48.04084 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 602adf53-fd13-38e5-8760-26d7416280a1 | -13.85737 | -46.25827 | 2025-09-05 04:36:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 76a74f54-136d-3ce6-8b12-843556debc53 | -9.69873 | -51.07056 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73096835-9b12-36ad-928c-81b49270884f | -8.86172 | -47.92207 | 2025-09-05 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c5e66c3-334d-3e7c-862a-b0dcf5bbc2f8 | -8.34141 | -48.30447 | 2025-09-05 04:36:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ccab7f60-dee0-31b2-a8a0-bcd6afaca004 | -13.74478 | -46.92719 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4dfa4837-f8f6-30a4-b715-805bfe9ea23c | -12.71989 | -45.07655 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2a051cee-4a39-377a-a8f6-3758128eee8d | -10.97579 | -45.95225 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 748aba49-52dd-3c60-927b-b8c3625109f9 | -9.33724 | -55.21124 | 2025-09-05 04:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| daee9999-baab-3d8b-ae5d-abdb0bf0c4a4 | -8.91383 | -44.17339 | 2025-09-05 04:36:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cc44207-fdf7-3b23-ab12-c47466895aaf | -10.09759 | -46.24372 | 2025-09-05 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efc96525-5ebe-3006-a3f5-4969314ab1a4 | -8.09118 | -45.33496 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a4e58472-9250-3801-8d21-ea7187f9b973 | -11.39533 | -55.3709 | 2025-09-05 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15cc193e-65c0-39a2-9033-2f48498aa067 | -13.52165 | -48.20487 | 2025-09-05 04:36:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e43514a8-ba88-376c-9a6f-d77e6b00863d | -8.08166 | -45.32554 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5810415-5ca2-32e6-abd5-b48913db3c56 | -13.861 | -46.25887 | 2025-09-05 04:36:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d57be2e-c69a-3840-9acd-c6e8105a7411 | -12.51195 | -53.83489 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d8eaff5-87e0-3144-8bda-3e490cb2f103 | -10.08269 | -48.06841 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b447283-83c9-3022-8fa3-705a86ad252c | -9.80086 | -48.31207 | 2025-09-05 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f33f8f3f-e6f8-33e0-bae2-328cc01c578d | -9.44278 | -46.80987 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 732d1b93-f21a-3343-8203-88ad7d399284 | -9.96522 | -51.64088 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6ea264f-0e46-327a-b426-71bcc8957ed7 | -8.48222 | -45.06372 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b9095dd-59db-3f23-bb85-5aab43c4efbf | -6.32491 | -58.17561 | 2025-09-05 04:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d16cdef0-62d2-3ef1-82db-f80eb4713dfc | -7.72126 | -50.32177 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d2009e1-3600-3215-8ec0-4aaaba69207b | -8.09415 | -45.33943 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db98bffc-ceb4-3cbf-94b4-66e2f7b96327 | -10.14215 | -46.23835 | 2025-09-05 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 440cf4b0-0a63-3b31-bc17-908774dd3ffc | -8.93979 | -48.64774 | 2025-09-05 04:36:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40f4421a-dd6e-3d43-b9cb-3a9b61607430 | -12.26471 | -50.15507 | 2025-09-05 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f15c908d-668b-3fc1-b8c6-2705f0d7db9e | -12.15643 | -49.07986 | 2025-09-05 04:36:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8dfb7aa-71b6-38ec-b999-4ddfb2bcb4a3 | -12.97265 | -48.07836 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6aaa414b-3883-3c63-b6a7-b1c0e450e9fe | -9.96815 | -51.64547 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0bf5fd02-a0ca-3019-9b2c-1c5ba809f6f8 | -12.87779 | -48.01564 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3a47be8-c20b-390f-855b-6036a41911ed | -13.47051 | -46.83506 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fd718a1-5dcf-3f84-88c6-d19451e616eb | -10.48543 | -46.75442 | 2025-09-05 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d9c3c8c-edb9-368d-b530-05817b812528 | -8.00997 | -45.43806 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a75bc8e-75c8-3e97-99ad-afff17c84a08 | -13.29691 | -46.81763 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd8ecbbe-f2ca-3bd3-a3a3-64e139acf73f | -11.09702 | -52.02298 | 2025-09-05 04:36:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9701f967-5af5-38a9-87a9-5341b6defa7c | -8.86839 | -47.92312 | 2025-09-05 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a8edb2d-db12-38b3-9192-6c59411bd982 | -11.39454 | -55.37532 | 2025-09-05 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63b5a45f-e541-3abd-8875-98d5c0846ad6 | -13.74124 | -46.92678 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d05dcf4-8aec-3b72-b01e-d0b754e91e94 | -10.98918 | -49.77257 | 2025-09-05 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d2571df-3c11-3138-8139-2e7780824348 | -11.58011 | -52.1739 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bda9fff0-0287-306b-83b1-5207782f28f6 | -8.75036 | -46.11041 | 2025-09-05 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8429756e-03a9-36da-9148-aa608f34fe18 | -11.40242 | -43.5965 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65ee1c5f-050a-3648-aadc-52a905a8c637 | -12.29461 | -50.01239 | 2025-09-05 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dba2c1c0-eda5-3371-b657-039b21d91ca0 | -11.38901 | -43.60227 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd3d9628-4cc7-331b-b4a9-3cfdf2863e27 | -9.88002 | -46.54573 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| affd619c-577f-3656-8496-6178da181c67 | -13.38345 | -45.73009 | 2025-09-05 04:36:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cab3f3d-a744-3808-8bdd-c62afa55c7be | -12.43903 | -44.75194 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f5f6fd6-e8cf-30af-85b6-fee219428d21 | -8.86207 | -52.01769 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c299de9-2e20-3ade-bf13-de1f5c697b54 | -11.59967 | -52.16848 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bacaa00d-2c6d-3b97-9c22-13b5bad38c83 | -9.44334 | -46.8062 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4aa92c6-b7ff-3fa4-b3b9-016187dd7bbb | -11.77246 | -50.64801 | 2025-09-05 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9212a97b-e79f-304d-b40c-94755348eb1b | -12.97235 | -48.0752 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06156308-88d2-3aaa-bb47-8253547b585e | -12.27142 | -50.1562 | 2025-09-05 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d216334c-0544-3e52-9f8b-94c807d96b07 | -12.87551 | -48.00788 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e86aa682-ba51-308a-b7c7-949dc4ac0cc0 | -13.75068 | -46.93599 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 085cb55a-cbd3-3db6-863c-e79b71b99397 | -10.98598 | -45.93291 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db005afa-1630-3206-8981-dd0360461245 | -9.07548 | -46.99822 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7ad61351-2438-3328-a349-c87254af7fdf | -12.8709 | -48.00768 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eaa4b667-7ce9-31d9-8956-a1f9d8a56d4f | -12.97995 | -48.07578 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2210a75-1ec0-3455-8490-d0324048a7f5 | -11.59895 | -52.17272 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e84b5dd0-99e2-3e9a-a84c-fd194de752f7 | -9.50523 | -57.82019 | 2025-09-05 04:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ccc7145-4180-3986-ac60-987d52204bc4 | -8.35115 | -52.52042 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3bf50906-cda1-3a65-8006-a3a08880b985 | -13.35271 | -46.83006 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ce2ae4d-a383-3266-97bd-116dbb165e5a | -8.86133 | -52.02213 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00e2b40d-4a23-305c-af34-53c7f22c8b1a | -13.73536 | -46.9178 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f404eed6-4d2e-3857-b0f4-75ada7d85d70 | -9.07153 | -47.00137 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 836e6298-aad5-34be-9c05-9b99b4690757 | -12.9721 | -48.08195 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adfb83c7-7fa4-3ee7-8fce-64a8903d8393 | -11.39468 | -43.59159 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0b57dec-8515-31fe-bcc5-faaea29803cc | -13.00601 | -45.22214 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README25.md)
