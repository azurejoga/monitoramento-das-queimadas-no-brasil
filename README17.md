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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f260ee9-784c-36bf-a8ab-4876e9561841 | -2.95942 | -49.5403 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17ae1583-7928-3131-8bb8-967365e5685d | -1.41375 | -52.109 | 2024-11-21 04:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 081d54c5-49e3-3d70-a142-da1899fa23f9 | -3.29024 | -53.84475 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2eb2231a-efef-31fa-9aa2-da54c4f39392 | -4.66809 | -46.40459 | 2024-11-21 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39fcd69d-57b0-3914-95f5-1c659f55f241 | -1.42793 | -46.01757 | 2024-11-21 04:08:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b7fdbb1-c4c8-31d9-9ebd-ee3dc309b880 | -1.72816 | -52.70178 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5a7ab88b-3100-376d-844d-a5222474a4d4 | -5.4312 | -45.34296 | 2024-11-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4ec25364-886f-38a2-91c7-f79fe94f0d2a | -1.71101 | -52.48623 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef084b97-1bad-3b27-9d7d-b857aebe3ff8 | -4.66698 | -46.53953 | 2024-11-21 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9ec54e4-573c-3668-b27f-4705c5ae4643 | -3.71148 | -51.83984 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cafb0fd2-ba0b-3171-a8b5-8e2ee86685a4 | -2.63573 | -46.21816 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75a8eb51-0ac5-3bce-80a7-3d68f0ebb7e2 | -3.30262 | -50.35833 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49c86c2e-f8c4-3164-8be1-935674d1baff | -3.21814 | -50.58453 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1107a971-c3e4-390d-9db5-a34ceccde62e | -3.23053 | -43.27015 | 2024-11-21 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a03a450c-5ef4-34b8-ba5f-7f07e5971f21 | -3.49242 | -50.44401 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab6d900c-fa03-37e7-8f16-200ea2005708 | -6.98621 | -39.65502 | 2024-11-21 04:08:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2afe0d34-71d2-3744-b7bc-d87348a92295 | -2.94337 | -45.19202 | 2024-11-21 04:08:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90db3e90-39ad-331a-878d-2e86c46ddd68 | -5.81794 | -43.79719 | 2024-11-21 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f63b9173-18c4-3365-ae91-6dce93a041b8 | -3.04269 | -49.46796 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9e00ae0-e533-3d70-bfe1-98926d333df3 | -2.62208 | -51.80785 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 574c4f84-5ab5-3632-936b-60681ac0612a | -4.41006 | -45.96139 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56e02dc9-af7f-376f-bc49-b44c52169b57 | -4.49282 | -47.10637 | 2024-11-21 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25c09c80-f555-3c9b-93ce-edae4ce0e1cf | 0.13916 | -51.08934 | 2024-11-21 04:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58d1c2cd-8caa-346c-93ce-a64f159c002c | -3.30742 | -50.36264 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b74ec3b-3c71-3b44-b3ed-c0c7460e47b7 | -4.12837 | -49.43562 | 2024-11-21 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a814658-da36-33ec-a483-ff265e78aa41 | -3.5037 | -48.22698 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afb2479e-8dad-3b6f-91ef-d11bfb4a6b5c | -2.96528 | -51.0217 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d15392ab-805a-3aae-930c-07cad5ea7939 | -6.20035 | -44.37149 | 2024-11-21 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 735990ae-ff56-31f3-ba18-bef719534f38 | -6.98275 | -39.65445 | 2024-11-21 04:08:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| df5411f3-4854-3689-a9db-91fc8e46b2f1 | -2.53426 | -45.4421 | 2024-11-21 04:08:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 95f72fb5-5354-332b-a434-4b32ef5ad039 | -3.04171 | -49.47383 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06ba5f9a-6396-3296-bb48-ea0cff531b33 | -3.27409 | -53.84114 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 43159b48-0fe0-3563-a032-ef90b38156b1 | -3.92685 | -51.18077 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78282524-902c-3b9f-88aa-12c5c897eeb6 | -5.27207 | -44.36824 | 2024-11-21 04:08:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a626f5fd-bb22-31a7-af59-0b0f26a2d114 | -3.32738 | -50.25755 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b676edc3-65fc-36d5-9737-296f75b03cd6 | -4.09765 | -44.85786 | 2024-11-21 04:08:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 222c87d2-a0b3-358b-aa3e-3eff20f87c77 | -3.81245 | -47.80324 | 2024-11-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b42292bc-c960-3c28-94bc-33dcfe2c4146 | -3.30359 | -51.29121 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f87307a6-3baa-35ba-8a00-6f2022529f95 | -1.22192 | -51.74331 | 2024-11-21 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5219fd54-3efc-3af8-bb08-f3a688e76af4 | -3.29128 | -53.83875 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 949da5f2-37e8-3a66-9129-8aa820006a2b | -5.38767 | -45.36545 | 2024-11-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5790e7e7-3277-3d1e-afa3-ba5ba355df7f | -1.06602 | -48.01041 | 2024-11-21 04:08:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1e99eff0-9fc3-3ae1-8d61-6da7dfffec95 | -4.98527 | -48.75198 | 2024-11-21 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 548e9a58-173c-338a-a978-e707fbd5a5b7 | -5.30124 | -50.56874 | 2024-11-21 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f851321-9f13-3f55-ab44-47d0f93418db | -3.81542 | -51.27103 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e21bd3e-c247-381c-a2dd-20fd880c6748 | -3.09788 | -53.21725 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 462c10f9-a8df-3901-9e70-325f14ed78cb | -3.55406 | -50.2768 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ca35530-64c7-3dba-97e6-dec77a9812eb | -1.23069 | -47.35469 | 2024-11-21 04:08:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 433e09fc-df09-3a97-b9e9-0bb75b8a0c4e | -1.63869 | -52.60701 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 902ba6e9-727d-3977-98ff-0315c09320d2 | -1.3748 | -46.51012 | 2024-11-21 04:08:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6916688-37e7-37d7-b792-ce87890d6f1f | -3.88757 | -46.6632 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 539ccaf0-cbff-3b4d-a9d8-58543e6accc6 | -4.49274 | -47.10716 | 2024-11-21 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6a49e13-9110-38fe-945d-aaec8f3e3de7 | -3.54504 | -50.52748 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 80bda4ed-01e7-351b-b157-c145221a0a0b | -3.80196 | -51.26616 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95199f76-ff29-3bbb-8e34-cffef83b23b8 | -3.60219 | -49.86609 | 2024-11-21 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a22f22f0-8560-33d9-b395-d2666552c66f | -5.23376 | -42.63985 | 2024-11-21 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3db2cd38-b432-35f9-bebf-1ddf07362137 | -2.76867 | -45.13815 | 2024-11-21 04:08:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 422611cd-0dfa-3916-a3d4-8d1bfc953c19 | -3.376 | -50.28297 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32b5c138-1417-381a-8192-8196ac089959 | -1.19842 | -51.77276 | 2024-11-21 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15cd98c7-c4e8-3864-81d3-091edd62d623 | -3.30204 | -50.36172 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55350be1-e6a0-3d24-8f88-0aed9875c5b6 | -3.88816 | -46.65953 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 865529a4-0fc8-3113-9411-94a583335e1c | -4.24845 | -49.08028 | 2024-11-21 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d7d4fd1-e249-365e-905d-431a44c5792d | -1.43443 | -46.00342 | 2024-11-21 04:08:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5af22d3-05e1-3d90-93d8-ca0b38a660c0 | -3.33524 | -50.49463 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e896a0a7-7935-39a4-b3bc-2e578bbe14d3 | -5.57914 | -42.60755 | 2024-11-21 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79563bb7-8d5b-3620-bd11-ff4456d4fa6c | -2.96591 | -51.01785 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e1f37e84-c658-3968-a359-34184311a814 | -2.84831 | -49.15297 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 198ecb31-33de-3e3c-abc3-de4fdf4ce781 | -1.1126 | -51.75723 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a7f68ff-384b-3fae-82b7-6ba534d34889 | -3.46368 | -52.72492 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35a5761d-78f4-3f1b-95fe-7e5dad920255 | -3.19104 | -48.57665 | 2024-11-21 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab330c83-50d4-3408-a108-557298728ffd | -3.26929 | -53.82856 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f0977258-2fbd-30b8-85f1-b207ec159eb0 | -4.66867 | -46.40098 | 2024-11-21 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ca86b2a-2b41-31c9-9527-eafc4d1660d1 | -2.63014 | -51.92237 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e22c9520-c84d-3b4e-8012-07e82e0f6739 | -4.15445 | -42.02079 | 2024-11-21 04:08:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9e9d6e6c-8f2b-3a4a-bfcb-54d1bcfe1230 | -2.63866 | -46.22617 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c07d5a3-ff3c-315c-963a-f266b49501e9 | -3.26404 | -50.61752 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6678393e-627a-3f71-9e49-3f79969573c4 | -4.07223 | -46.83719 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08d58365-2b80-36b9-9a17-32fdcbc56dc8 | -5.61915 | -45.09212 | 2024-11-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4789e759-33a7-390a-b3db-ce01307ce21c | -6.19693 | -37.4373 | 2024-11-21 04:08:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e8307028-4fe8-394e-90de-a162ba24db61 | -2.46033 | -47.03591 | 2024-11-21 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc0578f1-3735-302d-9d6d-5a43a2839d1b | -0.94918 | -51.71956 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ab688a7-5cda-3a12-aba3-c5ce1812a785 | -2.36907 | -53.82734 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1711ab3f-e963-397e-93c9-fa24e02b1cc3 | -5.45798 | -46.486 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 150e99c5-f5da-3d7b-9d5b-ca8b6faf9d02 | -1.12145 | -46.85313 | 2024-11-21 04:08:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56ba1e33-24a7-386c-9725-e57d72a6d6f3 | -4.48291 | -44.76621 | 2024-11-21 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7350680d-9240-32f1-97aa-6baf21d82e5f | -2.56113 | -46.55017 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8271c813-6838-384c-85da-578c30b5878a | -3.3834 | -52.45943 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4cedf9f5-8eb5-3ba1-b6e8-419f641442c4 | -3.27993 | -50.21218 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d869ce5d-de3d-3e1f-8740-eeef7c1004ef | -3.09883 | -53.21166 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| acf9bd95-d4e6-3d5e-ac91-213da3379131 | -3.46919 | -50.01322 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e80f7799-3596-304c-979c-ad4b32fa3f4d | -6.59662 | -41.97705 | 2024-11-21 04:08:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5e3b3eaf-5320-3f22-b424-ece2328324c7 | -3.29362 | -49.19772 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4b35516-27cb-330c-b867-b06295cfc8bd | -4.65155 | -45.40401 | 2024-11-21 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e9e1c5c-8467-302b-a32c-88adfc5db072 | -4.4748 | -45.65914 | 2024-11-21 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a799c77b-8383-30f9-b718-d052e05c6e70 | -3.6219 | -51.08985 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| acc4f16a-ec6d-3d49-a197-bb6c61661a87 | -3.48414 | -50.31309 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 575a3e40-cff6-3f66-92ae-39308be43f5c | -2.24551 | -46.81892 | 2024-11-21 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c45a5e2e-5bf9-3f61-97c1-ddcb436d9e85 | -1.19449 | -53.68093 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e117555f-0068-3249-9fda-b218ecd353ed | -3.60052 | -49.86839 | 2024-11-21 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bfb4546-d8d4-3ebe-bcbd-77c9b520771e | -3.77026 | -50.7038 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README18.md)
