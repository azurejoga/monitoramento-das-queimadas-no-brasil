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

## Dados Diários - Página 191

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9fe9314-349d-38b0-b20d-08bca52c9218 | -19.76441 | -48.27714 | 2024-10-09 05:06:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87770002-1f99-3af4-ba9b-d0f875129911 | -19.76401 | -48.28138 | 2024-10-09 05:06:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f276ef4-3992-314c-91c2-18a3e8f1bc4b | -19.76208 | -48.27742 | 2024-10-09 05:06:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce1aabdd-d291-3b51-a7b4-9a902649cc8f | -19.76165 | -48.28163 | 2024-10-09 05:06:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 284e280d-ed54-3d83-b6db-bfa2f410f422 | -20.45211 | -48.84035 | 2024-10-09 05:06:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 572576fa-f16f-32a0-9708-9d9885f93efb | -20.45169 | -48.83731 | 2024-10-09 05:06:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 247b4b78-8466-3c85-9866-22e702bcbee5 | -20.45132 | -48.84115 | 2024-10-09 05:06:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 570ed68e-e491-3b68-bf42-c4e9ee7341fe | -22.19167 | -49.6526 | 2024-10-09 05:06:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c84d355c-4dfa-3799-b0c3-6108114a23f0 | -22.18631 | -49.65186 | 2024-10-09 05:06:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3a86f5b1-e82c-3ff2-9116-f02774d64ebe | -20.56423 | -50.11041 | 2024-10-09 05:06:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 612c91f8-7f48-3504-a030-87b30cf5dad3 | -20.56391 | -50.1135 | 2024-10-09 05:06:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c33454f2-dc5e-315e-b03d-bbbcf076111f | -20.56327 | -50.11966 | 2024-10-09 05:06:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dc870153-65f8-3d51-bd2a-15abb183141e | -20.5588 | -50.11287 | 2024-10-09 05:06:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2952304c-17f3-3ebd-9464-1ccb8034110d | -20.55304 | -50.11846 | 2024-10-09 05:06:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 543d5ad5-5c30-3bed-b51b-b9ea9ff9404b | -20.55272 | -50.12157 | 2024-10-09 05:06:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f95c93a2-9f41-3f1b-9688-f5d49712c932 | -20.54826 | -50.1147 | 2024-10-09 05:06:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 00236e3e-c60c-3718-ae3d-c87bd68234bc | -20.54794 | -50.11779 | 2024-10-09 05:06:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 14abc3ac-546d-34cd-abb9-560008d44690 | -20.54762 | -50.12088 | 2024-10-09 05:06:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 313127cb-0384-3331-8317-9dd557943a21 | -20.5473 | -50.12401 | 2024-10-09 05:06:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1466d4dd-f6b4-3f21-a5de-fa6367c31e3e | -20.54346 | -50.111 | 2024-10-09 05:06:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3c0661c8-125a-3f0d-bc74-a05069ef8bfe | -22.66227 | -50.94523 | 2024-10-09 05:06:00 | NOAA-20 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9d9a4a1c-c7f0-366b-94f1-18ffcad3e64e | -22.66159 | -50.94383 | 2024-10-09 05:06:00 | NOAA-20 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ee5d1e6e-0823-3a11-8cf4-03eb4c123aa5 | -19.81562 | -52.2447 | 2024-10-09 05:06:00 | NOAA-20 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2fb80221-b441-3f36-95c9-66cde455a9a8 | -19.81121 | -52.24422 | 2024-10-09 05:06:00 | NOAA-20 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e6a6ac87-e953-33d2-b9d0-ed9ab9beddeb | -18.93282 | -54.55942 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abc8bb11-cfb5-3cb8-be5f-d74bd7313b68 | -18.93219 | -54.56416 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bcc3d4fb-039c-3938-98d2-11b56b45ca4b | -18.92977 | -54.55203 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd35e141-1624-3b61-942a-474e18789f5d | -18.92966 | -54.55421 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 35e489fe-4c33-39cd-8d53-2370771f6ba6 | -18.9291 | -54.55683 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f029ee9d-218e-3d50-9c23-881ed33078c7 | -18.92904 | -54.55896 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4412e31b-0c0a-31f1-853c-225a147729df | -18.92845 | -54.56156 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 21f87b19-cebf-33bc-977f-5d1d8c67f696 | -18.92841 | -54.56371 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 029af00a-b717-3e34-8e27-bfa368615b15 | -18.9278 | -54.56631 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fe237356-2542-36eb-a3bb-b8e52e4be515 | -18.92598 | -54.55159 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a4fe16d-1d8b-3f3b-a432-e4ff375e1d71 | -18.92588 | -54.55377 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41c7b221-92ae-3786-8523-124347b7ea06 | -18.92525 | -54.55853 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e26d0031-d579-373d-88d7-22fcbd9923ce | -18.92467 | -54.56113 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 75e45e95-3c23-35fa-a354-67b4f90a06f7 | -18.92463 | -54.56326 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 23.9 |
| abba8c65-56e0-3d11-88c2-f40bbeb518b4 | -18.9222 | -54.55117 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56dd60f8-bc48-34c0-a3f8-5774f834609e | -18.92209 | -54.55335 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 526da99e-4981-392f-ab2a-b995b28329d8 | -18.92153 | -54.55599 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3d10a48-37d9-3b27-87fe-fd5c2f56d3e5 | -18.92147 | -54.5581 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bf6a889-0d28-3b37-b9fc-243c5c7ff0c4 | -18.92089 | -54.56069 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c19ea6b6-bf0c-345d-b19c-1f1b80bed273 | -18.92085 | -54.56282 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8186909e-d022-3faa-b0d3-cbf491e67955 | -18.91836 | -54.58178 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 26.5 |
| dd7bebe9-436b-3218-b431-1929854d05ef | -18.91828 | -54.57963 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 16.7 |
| da0f2086-136f-3e3a-9568-44913832379a | -18.91763 | -54.5843 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 4677269d-380d-3d06-ac5e-b00d5fc84d7e | -18.91459 | -54.58124 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 26.5 |
| d44b0307-34b7-3b65-b615-dbab8398e683 | -18.91388 | -54.58374 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 17.6 |
| efa52b90-509f-35e6-95bf-071c692f508c | -18.91076 | -54.57851 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b74e8e7-4377-3c46-9692-3ebca610648a | -18.91013 | -54.58313 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c18dcbc-52c0-3e4a-b984-1fb949726eb1 | -18.90949 | -54.58778 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84d3ad35-ab4d-3f20-ad32-42c6eec9a9c4 | -18.90574 | -54.58715 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dabd0c2-4568-3755-b583-7d47e948a794 | -18.90199 | -54.58651 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11409d44-0df1-3ca8-9a00-78df2b448a2d | -18.89824 | -54.58588 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 492827d1-700a-3f37-85e4-22040cc0b494 | -18.89644 | -54.45747 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2a15f3e-9b45-3977-9f59-07f83d946e75 | -18.8945 | -54.58523 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8d58a03-e795-346e-802c-6a34a1045c66 | -18.89201 | -54.46175 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45cf5d4b-745e-349e-9971-a0d3d84419c0 | -18.87951 | -54.58268 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07e97a31-b92c-391e-b678-d7b9a456eb70 | -18.87513 | -54.58669 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 939ceead-d3dd-3458-9db1-a9b5463410ea | -18.87204 | -54.58115 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29d067c8-0acd-3235-a14f-15f3f0e364d3 | -18.87141 | -54.58585 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 838f0917-8823-3396-ac05-a0954df78686 | -18.86893 | -54.57579 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e62ab8bd-cf80-3ca6-a0b4-a2cfa72ec1ce | -18.8683 | -54.58049 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f78db866-3ce6-390b-8885-fcedd8ebe2b3 | -18.86518 | -54.57512 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f19af62-33a8-3994-b98e-a8b93ca4f6d0 | -18.86143 | -54.5745 | 2024-10-09 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71747e61-2155-3bd8-8725-ecbce7831e17 | -18.85788 | -54.4861 | 2024-10-09 05:06:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0782213-53f5-3b3c-a823-e588426b32a0 | -20.89526 | -54.9783 | 2024-10-09 05:06:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 286cfe32-508c-3908-94fe-a0d6f59bd6e8 | -20.89149 | -54.97768 | 2024-10-09 05:06:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 10cc413d-02be-380f-8a2b-ce73ef4fae6a | -20.4233 | -54.81985 | 2024-10-09 05:06:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d89aebd-cd69-3d29-9198-191919ec6e8c | -20.07436 | -54.51929 | 2024-10-09 05:06:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4125e267-d536-389c-b3f5-6269b8402348 | -20.07054 | -54.51872 | 2024-10-09 05:06:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3d5184f-c493-3e35-a90f-6a4ab22faa98 | -21.3948 | -55.68542 | 2024-10-09 05:06:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| efc42580-6b74-329f-b43a-9f12ce6d3b14 | -21.3942 | -55.68992 | 2024-10-09 05:06:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cff3e64d-cbf3-345f-b537-0a79276702c6 | -21.39115 | -55.68486 | 2024-10-09 05:06:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7018297f-e3f7-3289-bab0-8fb8d7dd8b2f | -21.39054 | -55.68943 | 2024-10-09 05:06:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 016c5f14-ac09-3469-984a-c1f110418268 | -21.38749 | -55.68431 | 2024-10-09 05:06:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5e6bb74-0ca3-39c3-83e4-c5179c20d126 | -21.38383 | -55.68382 | 2024-10-09 05:06:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88e69635-4539-3622-bcc0-119ec6cec82c | -20.10209 | -55.95196 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 23c79ff6-2c41-3b63-b5ab-96b27911aa6f | -20.09023 | -55.95881 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c29df37b-d8eb-3243-99eb-9116f57422a8 | -20.08311 | -55.9577 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5d0dd631-8c44-35fc-abb7-82b088cc95c5 | -20.0754 | -55.96085 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7d738313-e63b-381b-b9a2-dac7b84997bf | -20.07184 | -55.96029 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c179acc3-6edb-39e8-94ff-24335d7209a9 | -20.10505 | -55.95678 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| dd6016c7-ee86-3b27-9e63-2f21e2f81f8b | -20.10149 | -55.95622 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 9f11261a-55d9-37f5-9e4c-efb2479bbdd0 | -20.08667 | -55.95825 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 14fb0429-e6ec-3b74-8872-021a47f74fcc | -20.06532 | -55.95491 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f68eecc0-b3fa-3b65-9d9f-679c85728db6 | -20.06473 | -55.95917 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1ddd8e30-255b-39f1-9b3d-3d3b895cd3b1 | -20.27147 | -56.93868 | 2024-10-09 05:06:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 07357b7f-abc6-3f93-acfd-c2371f180e47 | -20.23845 | -56.97295 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69d8331b-f7a7-37bf-a564-bd1bb0814aaf | -20.23612 | -56.96479 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 795cf2f4-42a4-386f-82f3-26698b23791e | -20.09794 | -55.95566 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 35108182-f1bf-36e5-af24-9433b2ebc2ca | -20.09498 | -55.95085 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e8d7f08a-daef-3048-ad48-5b836dc05d18 | -20.09438 | -55.9551 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b8646e65-1d99-3495-aeec-f8561e1e6235 | -20.09378 | -55.95937 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b4a58311-debd-3056-ad36-7270acac0a21 | -20.09082 | -55.95454 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 583d4741-7820-31ad-b3c8-a6d73bac4f4e | -20.07895 | -55.96141 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| efb7316d-7459-3970-83f6-58e1511f8a3b | -20.06888 | -55.95547 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 68c6fd00-f3a2-30ad-99b1-8d6245e90540 | -20.10565 | -55.95252 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1380ba2f-b8c2-3739-8659-92a05d13032e | -20.09854 | -55.9514 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |


[Clique aqui para ver as próximas entradas](README192.md)
