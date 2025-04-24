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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ca18274-73c8-3a16-b91a-d113c420bc3c | -11.41149 | -52.95284 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c2c31cf-4c94-3ae4-8608-f578298ebf5f | -11.39812 | -52.95061 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e764698-4727-3c33-a587-955860a82ab1 | -11.40146 | -52.95116 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd0b48ef-da21-3fbf-a258-5e0493efe14f | -13.73894 | -53.38039 | 2025-04-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0251b1a-cbb0-3eda-932c-ab68df40d78f | -11.40595 | -52.9446 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a46d0ac7-8aff-31d0-8398-4d5983b8d2c1 | -15.07649 | -48.94491 | 2025-04-24 04:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d06e6bd-c43a-3867-a253-f907cea3ac41 | -11.52816 | -54.31925 | 2025-04-24 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 761ba583-cf62-3901-a5b0-10de5417b202 | -11.40423 | -52.95528 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b771d447-9b66-36e6-ae78-61b6956e9255 | -11.39983 | -52.93993 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c3c5ad5-0f1d-385a-9a43-6b733576853c | -11.40814 | -52.95228 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 167ad751-4bfb-383c-aef3-b26626a08fb4 | -11.39926 | -52.94349 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cd98438-701b-3faa-bc44-7cf606c55d4b | -11.40261 | -52.94404 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e37a5bfd-3433-3fcf-8e65-f2495414297b | -17.13821 | -46.85703 | 2025-04-24 04:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a997392-5d2e-38c5-a97b-024d1b43ee03 | -11.40366 | -52.95885 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8262e5c5-836b-3003-a5bc-033151a9d97d | -11.39869 | -52.94705 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c1b14f2-fe12-3cfd-a569-8f563593e123 | -11.41206 | -52.94927 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df3f047f-49c7-33d2-8dfd-37e092122e91 | -11.39754 | -52.95418 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44fbca8d-c68d-36e9-b980-744b1d12269b | -11.40872 | -52.94872 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbcd0d83-2b16-3bc8-9266-f99cd52f681f | -15.09199 | -52.84555 | 2025-04-24 04:49:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a128bf06-b8d5-3258-b3a9-b3e556c46b18 | -11.40757 | -52.95584 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0bac82e-34ba-3b8d-918f-55fb280bea3f | -11.4048 | -52.95172 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7ee8e86-d28f-3e6f-b7d9-46c89372d19a | -11.40318 | -52.94049 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e04e9d3a-ff14-3ce6-a58b-5fae4bf66905 | -11.40203 | -52.9476 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1c094e9-a529-3dc7-8301-69b9d24983a2 | -11.40537 | -52.94815 | 2025-04-24 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23f05a12-9e60-3438-a7cf-d4a9ea4e387a | -17.0123 | -52.5392 | 2025-04-24 04:51:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc96235d-de8f-3cfb-afd6-f4b3b59d16f3 | -22.48668 | -50.18966 | 2025-04-24 04:51:00 | NPP-375D | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 460f9ba9-7ab8-3bac-92c4-1bc741f12212 | -29.96273 | -50.97674 | 2025-04-24 04:53:00 | NPP-375D | GRAVATAÍ | RIO GRANDE DO SUL | Brasil | 4309209 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| e61b6c65-48eb-3934-9bc3-1ea2c51d3595 | -31.2169 | -52.06019 | 2025-04-24 04:53:00 | NPP-375D | SÃO LOURENÇO DO SUL | RIO GRANDE DO SUL | Brasil | 4318804 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 52c168e9-477a-3e4e-8945-ef4e96171ec2 | -9.62282 | -37.03029 | 2025-04-24 04:55:00 | AQUA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 9.3 |
| e84202c6-3def-30e0-9799-d40baa723ee5 | -8.86542 | -49.88641 | 2025-04-24 05:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4a32fe6-05b9-3d9b-b246-93709e92ac77 | -8.86959 | -49.89266 | 2025-04-24 05:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a189044-6e4d-3b44-ab1f-90d14ad0d124 | -8.86467 | -49.89196 | 2025-04-24 05:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba88e4e3-db3b-3365-87d0-b58444a51490 | -12.26774 | -63.82187 | 2025-04-24 05:10:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7619af00-68a2-3e36-9723-d23998833894 | -10.36064 | -59.02017 | 2025-04-24 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e37ed09-18c6-3813-ace0-b788f44c1a2b | -11.40259 | -52.94457 | 2025-04-24 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 86ab9cc4-3b2a-39e2-8c20-6cfd8f306c98 | -11.4098 | -52.95321 | 2025-04-24 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 38532aac-6c53-3083-b7b9-dc8922ecc36c | -15.09344 | -52.84789 | 2025-04-24 05:10:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd650ce4-e471-3ef1-b26a-56554efa65a8 | -9.16541 | -61.9523 | 2025-04-24 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bce738a-ade5-3d81-8cee-b1220d3a74b9 | -11.39845 | -52.94401 | 2025-04-24 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c1f4acc5-74f4-3db8-8400-e3eac3730e34 | -11.40099 | -52.95588 | 2025-04-24 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc677ed5-e7dd-3aed-8ce6-ae816841270b | -11.39791 | -52.94779 | 2025-04-24 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9c8be27e-4100-3fe9-bd51-e12bcbc89086 | -11.40513 | -52.95644 | 2025-04-24 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d66c896c-cb5a-3603-b8c2-266839169f43 | -11.39738 | -52.95156 | 2025-04-24 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bd39667c-5ac0-30e5-9bac-e13546d59f2b | -13.73594 | -53.37978 | 2025-04-24 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60f41769-e893-34ec-99a4-9ec6cbbdd4aa | -11.40312 | -52.94076 | 2025-04-24 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| af2b9487-ef18-3459-bbce-fdcef0cd0a1b | -11.4046 | -52.96018 | 2025-04-24 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d0ea4880-1ba1-3f7d-ab9a-81547af6d46c | -11.40205 | -52.94836 | 2025-04-24 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1581d48f-f64f-349f-81b4-7b60611fcd9c | -11.41034 | -52.94943 | 2025-04-24 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 276c6bba-dde9-32ac-89d5-705992407ff9 | -11.40566 | -52.95268 | 2025-04-24 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4e29e274-4a05-3e62-a4c8-5ef766378c64 | -12.36531 | -60.80479 | 2025-04-24 05:10:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef1bcf26-b274-32d9-855c-23de4eda4d82 | -11.3963 | -52.9477 | 2025-04-24 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| e9447511-eb5b-35d3-88b6-e5528a555533 | -10.0743 | -37.29569 | 2025-04-24 11:36:00 | TERRA_M-M | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 39e812bf-02ab-3ec6-abaf-b1cce94a77a7 | -9.63925 | -37.39163 | 2025-04-24 11:36:00 | TERRA_M-M | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 46489001-b458-3e15-8a8e-fcf7e28eb8fd | -17.41493 | -44.90857 | 2025-04-24 11:38:00 | TERRA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |


