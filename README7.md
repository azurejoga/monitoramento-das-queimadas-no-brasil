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
| bb7f5bcd-b10f-3642-a909-a7d56c9ef972 | -9.04254 | -46.98331 | 2026-01-10 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76adc911-1a2e-3af5-bae2-781d74887040 | -7.49258 | -45.57629 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 942027f5-d8ff-322a-9260-2ea862da0442 | -6.35868 | -46.15591 | 2026-01-10 04:27:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1755fc6a-193c-3257-b3b5-a146bf04c023 | -13.24993 | -44.11161 | 2026-01-10 04:27:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20653478-f974-30a7-af84-1da020e4712d | -10.486 | -44.93295 | 2026-01-10 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f57d1ec-a4a6-3dae-8e9e-47648c4a8895 | -7.49088 | -45.56516 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6025a8b-4b1d-35ac-8055-83dd70ae3a86 | -7.49204 | -45.57983 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2470426e-a747-3985-9563-43c9787c1092 | -11.83071 | -46.61043 | 2026-01-10 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f5e8086-477b-3a38-92ee-708d58cd3772 | -8.69219 | -40.76082 | 2026-01-10 04:27:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| abbcaa23-a71a-3e8c-b8d0-651fa3f1e9dd | -7.49142 | -45.56162 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b621daba-f160-3e72-9954-4f15c9e3d320 | -7.36244 | -47.02404 | 2026-01-10 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| db1f4720-49db-3a7b-af30-316fbacaae87 | -7.48925 | -45.57577 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d22627a-9568-33a2-b783-458cf2d56a9a | -9.0453 | -46.98731 | 2026-01-10 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbe32d7b-7fa8-3254-806f-0e15b4bd4fdd | -7.48762 | -45.58639 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ebfb0732-51b8-3e07-8947-cc4867e52a07 | -9.03923 | -46.98279 | 2026-01-10 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27527106-4c15-39bb-b375-f8920bb09ab5 | -7.49033 | -45.56869 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a52209d-55b8-3d93-a633-b796d5747f60 | -9.04584 | -46.98384 | 2026-01-10 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f487316a-8c56-3b19-b478-b6a637359c78 | -7.4887 | -45.57931 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 218cf015-1307-3feb-860d-abb8806d77b1 | -10.95608 | -45.06435 | 2026-01-10 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e97dfd3c-d57c-311a-82b1-a388449e71ec | -7.49422 | -45.56568 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9176ed96-2ff5-367b-8df4-bc5abe90a7ec | -10.79595 | -48.22466 | 2026-01-10 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 156271ef-b81f-369a-b77f-8c5004df2eca | -8.07359 | -47.13001 | 2026-01-10 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa1f7058-cc84-38b9-a984-e1f7658f3333 | -10.86119 | -44.28153 | 2026-01-10 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1bddd5ce-ddc6-31fe-95e2-97344d1a370e | -9.68995 | -37.10425 | 2026-01-10 04:27:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 49923dc7-e855-3ace-b28c-5cb535579924 | -11.83405 | -46.61096 | 2026-01-10 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78609e00-2be5-3180-8a84-e50b9396720c | -7.77881 | -45.83757 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 88d1acc5-db68-3eba-8f57-ff325165c299 | -7.49429 | -45.58742 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4327a365-aee6-3929-ac14-29b8e3f0f446 | -10.79263 | -48.22411 | 2026-01-10 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa90aa28-aad1-322a-bb9b-cd00b04eca95 | -7.72179 | -45.63393 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9241675f-e77b-3a3e-bb3f-f7b752226bd7 | -7.59757 | -45.88856 | 2026-01-10 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed36f99a-4dcd-3e42-8d2e-9a270982c7a8 | -11.8335 | -46.61454 | 2026-01-10 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c71760aa-59fa-3e13-9a23-bac9354d9c76 | -13.7823 | -43.23993 | 2026-01-10 04:27:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8f27325f-5d06-3109-bee6-0688711a0f2d | -7.49538 | -45.58035 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5709cc9-ac97-3c50-81d6-150e900dd59d | -7.49095 | -45.5869 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 01385859-10bb-38dd-8c36-2dd526b00c15 | -11.17527 | -43.30493 | 2026-01-10 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9ed59e80-41ca-3b66-98ac-057ebc2f4392 | -7.59703 | -45.89206 | 2026-01-10 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 744c9de0-b51f-35fe-85f4-f05842d6e3aa | -10.55926 | -46.91923 | 2026-01-10 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcdb2bf4-5ad4-32b7-8d20-ad8b6e209c31 | -6.35814 | -46.15936 | 2026-01-10 04:27:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ea698c1-82d2-3d52-9f8b-779086cd2924 | -7.69901 | -46.85014 | 2026-01-10 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7712ce0-b906-3ee1-b934-6105ed0907e8 | -7.60089 | -45.88908 | 2026-01-10 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abe72402-8f03-31af-ac51-091fd4e27b9f | -7.49367 | -45.56921 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0126edf-d1e6-3bf8-9d30-22aca3422965 | -8.18523 | -43.5763 | 2026-01-10 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b16c1f9-4af2-369b-8282-ad16ad4c677e | -12.19214 | -48.30558 | 2026-01-10 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 534bb1ee-c981-3521-9119-277a61312cf3 | -7.48816 | -45.58285 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1bba2d9e-b839-3820-a951-171e4bd306cc | -10.49006 | -44.92962 | 2026-01-10 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5b5e09f-917c-3dea-8bfd-448fb5a8daa2 | -7.49484 | -45.58389 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7bb50121-bec5-39b7-9e60-7ad7b38bc1b2 | -8.18947 | -43.5727 | 2026-01-10 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11fa183c-c103-3611-9e0d-6f2529f50e13 | -9.03869 | -46.98626 | 2026-01-10 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 000e67e6-29a4-3151-af47-4873fb294bb5 | -8.18885 | -43.57684 | 2026-01-10 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8607fa14-083d-35c3-9bac-ee8bbf49d002 | -9.05136 | -46.99183 | 2026-01-10 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b7d4bd6b-c164-3db1-90ed-5ddaec884605 | -7.4915 | -45.58337 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aadc8400-d8e2-3a6f-8b32-4092781782b5 | -11.82738 | -46.6099 | 2026-01-10 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca7ddd84-f9dd-3168-9af1-62841d4ec6e5 | -7.14768 | -45.25714 | 2026-01-10 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9e6148ca-a688-3e7d-a9ac-97d35c2720d4 | -9.98546 | -44.7554 | 2026-01-10 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29b73084-feb4-39c9-b786-f93de5b4995c | -11.9553 | -44.21124 | 2026-01-10 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11ed8224-9f0c-372d-a91c-d5f000901adb | -12.79778 | -46.41253 | 2026-01-10 04:27:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5cd923a-ae6e-3fa2-b2cb-098991e73e6f | -10.48659 | -44.92906 | 2026-01-10 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7e1fa0b-8d44-35bc-8cd7-e9921b4329f9 | -12.39802 | -58.04436 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 33f508b2-e303-3b1f-be16-557881f4e685 | -12.3883 | -58.03435 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d3331b3f-5a1a-3024-bc93-9a27bb191113 | -12.38753 | -58.03831 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 361150c2-e92b-36d9-8b1e-c80a7bca791c | -12.39316 | -58.03936 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3ca14f42-a6e7-38ca-adae-ad9cface3823 | -12.30252 | -57.36528 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc92eb1e-5816-3e5e-b192-59bf4891521e | -12.39659 | -58.03925 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| c15b66dd-e917-3173-b797-0a50f41927b4 | -12.40938 | -58.03363 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fde44ef3-9d51-36be-a1b9-cdb233525b6f | -12.29948 | -57.36841 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2bed785e-59e8-31e6-9908-5f2a9caa7d87 | -12.39738 | -58.03532 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 73f75929-74ea-3454-b33a-47a01a9358bd | -12.39954 | -58.03651 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 9adc9baf-023f-34f9-bcc9-28655b51361e | -17.42934 | -43.8236 | 2026-01-10 04:29:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe1ecc82-86c6-3b22-af4b-627c2c8c6de7 | -12.39651 | -58.0522 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f4661c9-6203-3576-bb6f-7b74c712257b | -12.30043 | -57.37582 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db6ac88b-85b8-3f38-ba0d-bc2d0c96c73f | -12.40288 | -58.0494 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 413f32da-c929-3dae-8888-23c90c425943 | -16.59509 | -58.21241 | 2026-01-10 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9cce3be0-8a60-3aec-bbe2-b77ac69a4cc4 | -12.38907 | -58.03037 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4d41c67-1242-3d53-a8e3-debd7443face | -12.40454 | -58.02865 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89f2861e-7152-3766-8969-1dc271b6115a | -12.30183 | -57.36875 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee24406a-9ee9-3c3f-a4b2-c52345d62328 | -16.83667 | -46.83621 | 2026-01-10 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55945966-d4bd-38e9-887a-069f83ab046b | -12.38939 | -58.04605 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 49dc55b3-1cc9-345f-b13c-0d438f4dc874 | -12.39255 | -58.0303 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0ab9556-2ab2-314a-aed3-38eedb5c0a16 | -16.4479 | -58.16188 | 2026-01-10 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| b45e39ed-382a-3f6c-9406-943a69c7220f | -14.32752 | -46.30271 | 2026-01-10 04:29:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31e8cac4-4927-3aac-ab43-262076adc7de | -12.38614 | -58.0332 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b4fef37-ed5a-3343-8643-7f478b76ed52 | -12.29158 | -57.39219 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a7fdd97-9a94-3a46-bb1b-be4bf82ac9cc | -12.40363 | -58.0455 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9f069256-ac50-3ec9-9bee-7aa738995993 | -12.39816 | -58.0314 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8cc622e-f914-3948-8744-2e29c447c61f | -12.4059 | -58.03371 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90c5a59d-79d3-3b46-94e1-ea50c427d19d | -12.39543 | -58.02759 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 391f79ec-182a-31b7-828d-05c9b698b1b0 | -16.59531 | -58.21534 | 2026-01-10 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cafb7e54-f86b-3e12-bba9-96661ec3e14e | -12.39878 | -58.04044 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 23e9da30-4e01-3aa6-b4db-92fbbdf20985 | -12.30114 | -57.37226 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1353b66b-0c61-3d2d-8ae1-ba9794f8f75e | -12.39176 | -58.03425 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 840bb17f-ee80-3797-992b-d75a42cc082c | -12.40299 | -58.03639 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b78e0a80-178e-370a-8221-9bcdffc5d292 | -12.29712 | -57.36431 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c7a0eb6-5f68-3376-b2ef-feacadc152dc | -12.39468 | -58.03147 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9b3191d-b925-3992-9d24-a8e7607298c1 | -18.00081 | -48.32499 | 2026-01-10 04:29:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7a532391-96fc-3d98-9978-8bb3aecb08c7 | -16.79306 | -49.30986 | 2026-01-10 04:29:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dd03dbbf-4aba-394c-a77b-f4ce66f1d169 | -12.39727 | -58.04828 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| def852fd-fe8a-3597-8019-1e61c11430bb | -12.39097 | -58.0382 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 235b491f-441f-33bb-a1b5-d9795f9fa555 | -12.30351 | -57.37662 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f24e9aea-268b-3ce7-9cde-acd374b3c13c | -16.75603 | -49.17826 | 2026-01-10 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b2799e0-fca9-3585-b30b-21010bcd0984 | -15.48204 | -48.95154 | 2026-01-10 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README8.md)
