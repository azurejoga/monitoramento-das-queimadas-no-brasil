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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed3b6e0b-d815-3c80-8fa9-ee2d99847d1f | -9.3609 | -64.33119 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5d4f878-49cf-33ed-a51e-50a9f12ec67e | -9.36077 | -64.33264 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7879bb8-9236-331b-9b9e-8d009664e702 | -9.30862 | -65.38007 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d184d83d-1ab7-34b4-948f-9b966663023d | -9.3081 | -65.38368 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81108b21-72b8-3d44-84b1-49990f421974 | -9.30507 | -65.3758 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f84bee9-a1ff-3ee3-8bc4-cd209be159a4 | -9.30454 | -65.37945 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa3202ec-2702-3ffa-9bdf-3b3e598abdec | -9.30401 | -65.38309 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 349f683a-74fd-307c-b730-710e0671f415 | -9.2937 | -65.51475 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e562ace1-1de6-356a-a83a-58aa864d1ad7 | -9.2932 | -65.51836 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f798b5b-2b0d-3aaf-a8a0-dde2e0e255bc | -9.29267 | -65.51814 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e7ea7d6-3518-359a-b671-1f44390c18f0 | -9.29043 | -65.33239 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 676ce93d-6554-3316-9615-7e3e4cbfcc2e | -9.28952 | -65.42561 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b19b0897-2a5c-342b-978d-94f7455b6a5f | -9.28546 | -65.42496 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 486c80b8-78a4-3914-9336-7ca81144dee9 | -9.28191 | -65.42074 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c502ead9-f69e-3714-9802-332ca051b913 | -9.26929 | -65.36331 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85fa2e22-810e-34a4-b1dd-84df19b3fbb7 | -9.26878 | -65.3669 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfa60356-c67d-32f7-97d9-91c2b67230e8 | -9.23888 | -65.605 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3bdaccd-4540-3437-a16a-72e1bfeebd6f | -9.23837 | -65.60855 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32956f09-0394-33cc-bd15-43684728a465 | -8.65688 | -64.29704 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6ac5a97-3fb9-394c-b9ed-230d4b1a0cfa | -8.65252 | -64.29642 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f43d17f-83e5-3f68-ad9f-e836e73b7c30 | -9.95414 | -65.24808 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d10d8ad-feb0-31fa-b580-9289ee102c05 | -9.94997 | -65.24751 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65ddd2b3-220b-3a20-8022-c60b97bc080d | -9.68753 | -64.62923 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 44556977-3927-32bc-a1f8-2808982e853f | -9.68696 | -64.63338 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 390c00e4-63ec-3008-ae0f-8d86fc910b4b | -9.6832 | -64.62865 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.4 |
| b43c72c0-da6e-37ab-be5d-2866c9fd817f | -9.68263 | -64.63277 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 49e33eb8-9226-35fa-869c-bfee951a78af | -9.50579 | -65.60048 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63e2a641-ecaf-3db7-9fb7-157d611b3a46 | -9.50529 | -65.60404 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cbf37357-5c8c-3ce7-aece-2612e4f8cf88 | -9.37847 | -65.47186 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bdb466d-3bc8-30ef-a3c1-2c31930dd738 | -9.36818 | -65.51466 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9db1a63-690a-33f0-8c22-dcfdb0b6ffb2 | -9.36413 | -65.51405 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54749a13-362d-37a6-8c53-3a395c819b6b | -11.54254 | -65.13914 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9406cd82-aaf7-3440-a2a2-5c468228e37c | -11.53208 | -65.05364 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 77b69a82-424d-30ce-80df-513e16457799 | -11.52776 | -65.05303 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 598f6476-0e10-3fb9-9dd1-80dca14c8fbe | -11.52721 | -65.05717 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c9759278-a901-325c-9cb0-5d77968ad064 | -10.85626 | -69.39301 | 2024-10-06 05:59:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d20ba57f-967c-395e-a4fd-ccd35110f3ba | -10.8334 | -69.56541 | 2024-10-06 05:59:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7b7a485-8bc6-3f70-8248-9dc3ffb6dd1f | -10.83004 | -69.56488 | 2024-10-06 05:59:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 88579661-8510-334e-8ec0-77ed68108707 | -10.63028 | -69.6312 | 2024-10-06 05:59:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c61e536-6cb4-3c75-8831-9e1b04373f80 | -10.62692 | -69.63068 | 2024-10-06 05:59:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2413b0a-a0e8-306f-887d-137aaad6a38c | -7.46854 | -72.6839 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6210b0ef-08d8-33bb-856c-1c89ab247907 | -7.46791 | -72.68779 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2683f530-7f41-391e-bd45-d6357ac55701 | -7.46506 | -72.6833 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a2fad79e-7634-3f6d-bd62-c89982615632 | -7.46443 | -72.68718 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 79020288-9892-3a31-b3db-35b57fd5953b | -7.46094 | -72.68658 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| edfbd9e3-de0b-3aab-b590-e377cef3e0dd | -7.34925 | -72.90337 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e13a448-b203-38e5-b18e-70a04b2aedd1 | -7.27562 | -73.06404 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dd7c28b-b627-3857-af35-7c9c87b6d45b | -7.36511 | -73.22417 | 2024-10-06 05:59:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ef7ed87-cf31-3dac-8991-8872ba267078 | -7.36154 | -73.22356 | 2024-10-06 05:59:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85cfef28-d088-3d82-ad5f-8a1b240360ba | -8.71292 | -66.65052 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e77a6c69-b978-3a51-ac54-7e88b5334b10 | -8.69148 | -66.65837 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2a2c43d-ff86-37b5-90cb-7bc2ba69c55b | -8.5473 | -67.12231 | 2024-10-06 05:59:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de86f128-5c7f-3d95-bc8f-7a9106de3c79 | -8.54667 | -67.12659 | 2024-10-06 05:59:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bf42d6aa-e2b7-30a8-9b80-0142253d406c | -8.54604 | -67.13086 | 2024-10-06 05:59:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 37f0b370-6e77-3df0-9beb-f8a0853883a1 | -8.05175 | -65.98447 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 934d94d1-1b93-360c-9802-5a019eeeace8 | -10.02013 | -66.9575 | 2024-10-06 05:59:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da695f12-34b2-3906-8089-a2b132c62bae | -6.19161 | -67.81795 | 2024-10-06 05:59:00 | NOAA-20 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b63c397f-d9cc-3bbd-93fd-d938ec8008b2 | -9.07483 | -67.66398 | 2024-10-06 05:59:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 841220f7-3bac-325c-9ae0-639c9f1fa86c | -9.715 | -67.73212 | 2024-10-06 05:59:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4e1bad0-867a-366c-b3cb-bac44777ca47 | -9.71439 | -67.73621 | 2024-10-06 05:59:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1702342b-580f-3226-ae1d-fa1287b79d05 | -9.71142 | -67.73159 | 2024-10-06 05:59:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e88c17ff-fc52-36f5-9397-c4e181315eb6 | -9.71081 | -67.73568 | 2024-10-06 05:59:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e25fa46-c052-3f6c-8514-d7513fd71dc7 | -10.86292 | -68.24467 | 2024-10-06 05:59:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86890120-f6a4-3965-844f-7c1d87d00426 | -10.85939 | -68.24413 | 2024-10-06 05:59:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2809fe14-1394-383f-9dff-7e89697015d4 | -10.53252 | -67.74135 | 2024-10-06 05:59:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 55f11c8e-e76f-3c8a-8bf9-7394c10ea122 | -10.52891 | -67.74078 | 2024-10-06 05:59:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 34ade6c0-b261-3b31-8ada-982a1dc19948 | -10.50026 | -68.66765 | 2024-10-06 05:59:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91447856-be21-3aa6-afa3-cd20ba7ae285 | -10.45853 | -67.88124 | 2024-10-06 05:59:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a265fa97-ae14-36f5-9f80-16ec2409fb12 | -10.45791 | -67.88538 | 2024-10-06 05:59:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6242b18a-2ef3-3c11-8aff-412782c50594 | -10.36387 | -68.17509 | 2024-10-06 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2266191-1c00-301a-984f-720c51c2e985 | -10.28818 | -68.02869 | 2024-10-06 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00738569-fd92-3d80-b29c-fb5957cde387 | -10.28757 | -68.03275 | 2024-10-06 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fd628d3-7783-35c0-85e7-f5e401f44ea0 | -10.24719 | -68.20753 | 2024-10-06 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 321edc63-e6aa-37b7-8ac1-4e67fe20b708 | -10.10583 | -68.06498 | 2024-10-06 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb1adb1e-7630-3f47-93f5-2f7e4c2dccdf | -10.10523 | -68.06901 | 2024-10-06 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f01f2f19-511c-344c-aa33-809ba1d5c163 | -10.10234 | -68.28349 | 2024-10-06 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 03fc2def-0deb-3e6b-8ef2-c7e94448e38c | -10.1023 | -68.06444 | 2024-10-06 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfa048f3-82aa-35f6-93fb-704445ec9974 | -10.10176 | -68.28744 | 2024-10-06 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 293f2222-4b54-3325-9b0f-89338f2f23dd | -10.09884 | -68.28295 | 2024-10-06 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6a7ac1c-08a7-31aa-b865-2eb513c92130 | -10.05972 | -68.37025 | 2024-10-06 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1b21249-dd10-3779-93f0-3ca822a58e4f | -10.05912 | -68.37415 | 2024-10-06 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0b520b7-d706-3a25-9e1a-4672fdf2f47e | -10.05623 | -68.36971 | 2024-10-06 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e21d541c-eee7-3e5a-972e-5851e046903a | -10.05564 | -68.37362 | 2024-10-06 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a546dec-8c93-3eb0-8500-ec63ec3f2412 | -10.65791 | -69.1324 | 2024-10-06 05:59:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad62dde8-2712-31b4-9a92-0b5af28835b6 | -10.63298 | -69.15897 | 2024-10-06 05:59:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 039436d3-70c5-3ffe-a051-1f306f0820be | -10.62958 | -69.15845 | 2024-10-06 05:59:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b26b8ac7-9258-356c-afee-e7cdbb6b16ea | -10.58087 | -69.06365 | 2024-10-06 05:59:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f4abab0-95d3-3362-91ea-5260dceb11ac | -10.5803 | -69.06738 | 2024-10-06 05:59:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a53f0bb9-899b-3f01-a2fa-e204bb560567 | -10.57745 | -69.06314 | 2024-10-06 05:59:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6971151c-77f6-349c-9133-c1793c4f6917 | -10.57688 | -69.06687 | 2024-10-06 05:59:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04091dfb-4f2e-3947-bb9a-8f1f6d163124 | -10.50085 | -69.13151 | 2024-10-06 05:59:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 473bfefd-c644-33a6-b58b-50263ae2756c | -10.89059 | -69.12099 | 2024-10-06 05:59:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35bdb7e3-67bd-3822-8df6-8795cad9e95e | -10.88717 | -69.12048 | 2024-10-06 05:59:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bff4542-6dc6-34e3-af02-9bda42afff89 | -10.92735 | -68.42121 | 2024-10-06 05:59:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c79aa432-68e7-3625-844d-e5eef436e83e | -10.92665 | -68.42213 | 2024-10-06 05:59:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af311451-03b1-3b8b-a12d-2201c6fb7487 | -10.92133 | -68.24107 | 2024-10-06 05:59:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cc280f4-3979-3beb-adbb-c704a70370e7 | -10.90766 | -68.28436 | 2024-10-06 05:59:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45909e68-7c29-382c-8daf-5abf8bee8af5 | -10.90473 | -68.27979 | 2024-10-06 05:59:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2624906b-2179-369d-aaff-317e82a5a7e6 | -10.85691 | -68.6484 | 2024-10-06 05:59:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96405094-42f5-33b0-8bf0-9aba62adda77 | -13.40565 | -61.9486 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README155.md)
