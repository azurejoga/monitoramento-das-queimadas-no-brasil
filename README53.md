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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6131cb30-647f-3fb9-bb6b-835f4f34b731 | -10.95668 | -45.96272 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cb90c83-1e2a-311c-9b61-53bb06a374a3 | -12.32449 | -47.04812 | 2025-09-05 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c19bfe7-a54b-3515-8537-6df40d934863 | -10.76311 | -48.29494 | 2025-09-05 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ba025b2-66d5-37e9-9a08-e5aed5e12b5f | -5.86319 | -57.77235 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 517a16fd-4891-339b-9378-46fdeb49504f | -6.27215 | -53.44091 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13d05932-f10a-3533-bfac-002c36b6ad92 | -12.98598 | -54.81242 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa5cf585-98b3-322e-a7c2-b0864dcd8db2 | -10.98702 | -45.93842 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7194139-e92b-3f52-99ad-131dff463848 | -7.61006 | -43.84523 | 2025-09-05 04:57:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02a81bd4-7efc-33ad-bfc6-3e5e7d8a58e9 | -8.6573 | -68.77475 | 2025-09-05 04:57:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa4a0bce-4872-3d25-9c28-4d439b9a932a | -12.94227 | -48.05248 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41592736-b023-3e8a-b955-b845d32517d9 | -5.86478 | -57.77568 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ab81b89-42ac-3aa4-9e66-093b25eb7b2d | -12.48248 | -53.83974 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 818dc0c6-0cb2-362b-8760-5b8799cb642a | -8.01964 | -45.41619 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0795710-e51d-344d-a018-6b5234df82e8 | -12.87502 | -48.00652 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fce9a7a-fd3c-312d-9389-45586d5072dd | -10.9752 | -45.98948 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78cc1eae-48d5-3f79-bc13-432259d82147 | -10.75915 | -48.2896 | 2025-09-05 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e340f55f-0a52-3e62-a94e-a0b640187db6 | -8.7815 | -49.63053 | 2025-09-05 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c0640f7-ec8c-3e8f-a136-a4c01f5aa8af | -11.10175 | -52.02508 | 2025-09-05 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abbbbfa8-75df-3f88-bf0b-2ddfccab3d9f | -8.86571 | -47.9188 | 2025-09-05 04:57:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c68c458-4c95-3519-a7a6-c788117fbd4d | -7.69788 | -45.1823 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 286f25e7-2a4d-36fb-b10e-37aa4975b68a | -12.89632 | -48.03102 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5f0b040-f2bb-3e6e-ba3f-007f7dd69d5a | -12.94637 | -48.05871 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cae78915-20b4-3c64-a5f3-81174f7ae815 | -9.82196 | -46.65894 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43ecb486-710a-3e20-bbb6-d4acecb4e466 | -10.4686 | -53.62141 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bee8acab-483b-34b7-a7dd-e8236a951bc6 | -7.75396 | -48.78649 | 2025-09-05 04:57:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a0b6fe8-0a5d-3e84-a08b-adec2ec3b8b0 | -12.9156 | -48.03291 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 496ebb71-e9bb-3f28-892e-91e929514e3b | -13.10506 | -57.10807 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62daec7c-5e74-3fe6-a589-9c13d7a4f1ac | -7.88911 | -45.30764 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b11808b8-15ce-3689-8a12-f8274220f69d | -10.09619 | -54.78054 | 2025-09-05 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab7f8774-b365-3829-a67b-a3ec3e89bdfa | -10.4312 | -50.26062 | 2025-09-05 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74c1f4b9-eb1b-3bf6-a5be-2aef3d3dbd5c | -12.18668 | -53.89835 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b299b615-2514-3cbd-8a7a-8fa0c615e627 | -9.06964 | -55.00209 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cf2bc4d-6bed-3562-90d0-50dc8031a732 | -11.59901 | -52.14871 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39fe9bb6-3bea-3944-b424-a317bcad6aa4 | -7.72525 | -50.32219 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fd68f02-af92-3908-8403-cc05e5f455e3 | -10.97926 | -46.00066 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92e08a15-685d-35f3-9117-7b549c6d0f44 | -12.90395 | -56.94334 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76d5f73c-5664-3c10-9eda-73d900576d9a | -12.9663 | -54.76904 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0d41e1a-99cb-3a15-b091-ebcd59a65e1b | -9.81691 | -46.65828 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b24f9c97-6424-3766-9edb-579ebec1f70f | -5.86184 | -57.77048 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52a507c1-7e31-3f25-932d-7e161e77d228 | -8.52015 | -51.33178 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b62e37f9-6e9b-346d-bb79-4766a01d1c88 | -12.97373 | -54.8031 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fd39cda-156e-3e0b-a27c-ce23f82673d2 | -10.48743 | -46.75458 | 2025-09-05 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6daf65d5-c94c-36c1-bb1d-c07112caab16 | -10.44942 | -53.61088 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa3522f3-45ce-3c16-8f4f-1f1342a3a44d | -12.32718 | -47.05224 | 2025-09-05 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3d665b3-3c84-3faa-9c5a-67c74a985d45 | -9.70957 | -48.98716 | 2025-09-05 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8152274-4fcf-304f-9145-4a847054e335 | -10.98743 | -45.93508 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f330440-cb8e-31b7-98f8-10ca83dd75ba | -9.20661 | -57.09416 | 2025-09-05 04:57:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48bd373d-89e0-37ae-b40d-0b41835634f8 | -12.96574 | -54.79473 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 78bf47c8-29bf-3724-a6cf-c4f4326d37e1 | -7.98257 | -44.52258 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 70c3bcf3-5c95-3a01-aecb-af6fb1b20d9c | -13.08646 | -57.11619 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b060492-7172-3149-a2da-a1e290641852 | -5.85887 | -57.76548 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62eb13fa-631b-3dbe-a565-d18ed31b9c14 | -11.62155 | -52.20256 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 831f82b8-7d13-324f-aa4b-0351c00a7d5f | -9.96712 | -51.64613 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c5ffa8f-88be-3b2f-bddd-c6ef4208c6a2 | -11.39182 | -55.37286 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4117be5b-373a-3eb8-9b81-e6efad049bbe | -8.01182 | -44.7741 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ee009c3-5a5d-32cd-8617-9c49d6b1cf9f | -7.23196 | -56.8519 | 2025-09-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43ce2927-d8ab-3aec-b716-1dc1536eb193 | -11.62757 | -52.21212 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 27378d6d-ba7c-3386-bb37-cb8f5b247bea | -12.01859 | -43.78524 | 2025-09-05 04:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bd8f85b4-3506-3d8d-85b7-870e35d6c3ff | -12.39692 | -54.96007 | 2025-09-05 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 332b9e69-50c7-346e-b478-d8c75b9b33b0 | -7.98876 | -44.51943 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d034964d-fdca-3afc-8690-e2be6d2e923e | -10.97243 | -45.96783 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ccd5c00-602b-37e9-ba32-e443a20eb078 | -6.32997 | -58.17256 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25aa1c76-c552-3ec9-ae11-c00c42449a7f | -11.64766 | -54.53885 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d54ff35c-572e-3c70-b3fe-c8c5e603cc83 | -10.9697 | -45.96781 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bceb52c4-c5d0-3a16-b30f-3b7d4bed09cd | -9.80195 | -48.30943 | 2025-09-05 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b83479f-26d8-34a2-8669-1466f54f94e7 | -11.60201 | -52.1535 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8666ee9a-133a-3968-bdd7-5c2edd00c1bc | -9.51221 | -57.81813 | 2025-09-05 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03b8f181-9ba5-3775-ade2-ecff8b83209d | -12.97817 | -54.79645 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca8e13b1-0199-3748-ac06-e501fc127281 | -7.89303 | -45.23766 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40c051cb-a11e-3d1d-a61c-05e41c2106ba | -10.47481 | -53.62615 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6521c01b-9d4e-32c9-8570-e8edfd0069da | -8.07892 | -50.20292 | 2025-09-05 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0eff8e8-6123-37f9-99d6-2b96732e4013 | -12.49951 | -53.84244 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a6fcd8d-4797-3941-ab8c-23325659ef1d | -10.87588 | -55.73471 | 2025-09-05 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe96aa6a-a409-3c4f-a5ed-7c4b6e744f43 | -12.51428 | -53.83706 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7c8b942-1314-3e37-b39a-aba71cfac086 | -10.47819 | -53.62668 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ad0e363-0d50-3bd6-bf73-8af7b2250063 | -9.41568 | -46.80125 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a1e126e-6008-31b3-968b-d9f9fdb2efc6 | -9.97579 | -51.63818 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1799185e-629e-39f9-bab9-b921d2fe0ee1 | -8.4835 | -45.06556 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54d60203-8d42-3ea2-86cb-a0ae97ddf010 | -8.01744 | -44.77456 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 557a61f7-01f6-3ce8-937e-e1bc66c0b714 | -13.29607 | -46.84454 | 2025-09-05 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0d68f31-c56c-3098-b344-1a46ad735131 | -10.15869 | -61.13544 | 2025-09-05 04:57:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 06256c1e-b69d-30a2-8c63-f95f8f1f92c7 | -8.08831 | -45.33375 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d1a9e06-24a6-387c-b04e-2dd03083171d | -12.51769 | -53.83758 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2268e3d6-c82e-39ea-a100-ef2cc3816804 | -12.85583 | -48.00785 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 392641c1-3ce9-3fc3-92c0-8198da9c016e | -9.79919 | -48.30966 | 2025-09-05 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e49900a3-0336-348d-bfb2-513cca24cd18 | -7.69033 | -50.29336 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ceb695b-4b9b-3979-a4d4-a05034d276c8 | -12.27434 | -50.15998 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab1bd23b-8269-3598-acda-82928c693bc2 | -11.72165 | -48.34805 | 2025-09-05 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58d3faa2-bab7-3d24-910b-d5d178666371 | -13.87162 | -48.0167 | 2025-09-05 04:57:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e30de99d-e615-3fd5-a56b-5cf2a1e0762a | -10.97182 | -46.82589 | 2025-09-05 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c458736d-a3c0-3aaa-9cf7-db1f8cee59e5 | -9.6216 | -55.35567 | 2025-09-05 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47b2b4c1-9640-33f6-b58b-1bb537c49480 | -8.06453 | -52.37696 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f685401c-d0ce-31d9-9d0b-eb45b78b323e | -12.98312 | -54.76408 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5ab1a16-f239-3b34-8545-ae415433fc5a | -7.02131 | -59.65811 | 2025-09-05 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74949a23-9ab1-3cb6-a1c7-a8b247a03e05 | -12.90852 | -57.0002 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a42a2040-9ff1-3c40-817a-e522bd324ca2 | -7.98927 | -44.51557 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6d86c4b-f1ca-302c-920f-14ee869f363d | -12.98433 | -54.82317 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a29fd1a6-d6ea-3ef2-ad1f-968236ae5eed | -11.5449 | -47.31508 | 2025-09-05 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a694ec3-4205-311a-b082-2cfd25a5765d | -10.49821 | -57.77369 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 798370e3-8bde-31f4-9245-2b599adefbe5 | -10.75849 | -48.29149 | 2025-09-05 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README54.md)
