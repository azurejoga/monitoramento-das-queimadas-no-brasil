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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f45b0d25-e177-3fec-92d0-cf61d388a7d8 | -20.00163 | -44.51867 | 2024-10-02 01:24:00 | TERRA_M-M | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.6 |
| 6177b944-c032-370d-99d5-ac796fa80724 | -22.90623 | -45.096 | 2024-10-02 01:24:00 | TERRA_M-M | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| 57eda086-2f4a-3949-aaba-1a4e02382a36 | -22.89842 | -45.10343 | 2024-10-02 01:24:00 | TERRA_M-M | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 153.8 |
| e096d0b1-705b-3ca6-8b49-4559e98c94d2 | -22.89686 | -45.11942 | 2024-10-02 01:24:00 | TERRA_M-M | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| 589a6b5f-5762-3063-9ad1-33df54368852 | -22.89419 | -45.08081 | 2024-10-02 01:24:00 | TERRA_M-M | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.7 |
| f54d9b06-07b7-31a3-b3a6-e9b45a189552 | -22.89271 | -45.09807 | 2024-10-02 01:24:00 | TERRA_M-M | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 198.2 |
| 690cfcb2-b13b-3a39-bc77-fe0af305a52c | -22.88473 | -45.1045 | 2024-10-02 01:24:00 | TERRA_M-M | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.7 |
| a8949f65-539b-3abf-9af4-b1fc267af65e | -20.52692 | -46.28731 | 2024-10-02 01:24:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 40.9 |
| bfbf9738-1733-3dfe-8fa7-6cbcbb5fcce8 | -20.52505 | -46.28158 | 2024-10-02 01:24:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 58.0 |
| ce49baf1-d7d5-3e2f-b154-0d44e9daff56 | -20.52312 | -46.266 | 2024-10-02 01:24:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 56cb3cf1-e969-371d-9d7d-d76b755742db | -20.52195 | -46.33393 | 2024-10-02 01:24:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 27320703-a0a0-3b87-901f-a05857ec4f31 | -20.52031 | -46.32762 | 2024-10-02 01:24:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 45.6 |
| b07e94de-0204-35b1-903f-946dea26fbf2 | -20.51785 | -46.31111 | 2024-10-02 01:24:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 7cfb4c61-2961-3234-bfc5-5d49b1248e5e | -23.51106 | -47.22914 | 2024-10-02 01:24:00 | TERRA_M-M | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.8 |
| fedd69a3-6508-3940-b379-5c1af1486d27 | -23.356 | -47.01101 | 2024-10-02 01:24:00 | TERRA_M-M | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| b572b3f5-53c6-3618-8d21-eade4c1b1d62 | -23.34821 | -47.01769 | 2024-10-02 01:24:00 | TERRA_M-M | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| f18a77a4-589e-3694-83c0-2e67ec32dc6b | -23.3232 | -47.27959 | 2024-10-02 01:24:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 6f1561e5-7834-3394-83eb-dc2087db824b | -23.32035 | -47.26347 | 2024-10-02 01:24:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 8900ae10-d445-39e1-b7ef-653bae0cb996 | -23.28141 | -46.66642 | 2024-10-02 01:24:00 | TERRA_M-M | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 8571fdb7-48ef-34fa-8e39-3fe1834bc42f | -23.27814 | -46.64859 | 2024-10-02 01:24:00 | TERRA_M-M | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.5 |
| c97bceea-fd7a-31f3-8c95-de33deaee02a | -23.27278 | -46.65522 | 2024-10-02 01:24:00 | TERRA_M-M | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.0 |
| d62ae7fc-baad-32ee-8191-f58a99acc8f1 | -19.24668 | -46.8758 | 2024-10-02 01:24:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 78cb4312-9b84-3852-9105-38b15878fae7 | -19.24359 | -46.86094 | 2024-10-02 01:24:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 226920a2-52c5-3983-859c-a53511a4012d | -19.24296 | -46.8554 | 2024-10-02 01:24:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 6646e780-433a-3067-990b-03fefd79bc3c | -19.2345 | -46.88379 | 2024-10-02 01:24:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 02621306-608f-3e6d-a484-57a54dbe0784 | -19.23404 | -46.87837 | 2024-10-02 01:24:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 038210ce-eb95-3cb2-a6a1-7f892edbb735 | -19.23094 | -46.86354 | 2024-10-02 01:24:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 257.6 |
| 9befb821-e007-3c6e-af9d-cc11745c184b | -19.23032 | -46.85809 | 2024-10-02 01:24:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 8042182e-03f6-32f3-a2df-f0d622606fd5 | -22.09318 | -48.47291 | 2024-10-02 01:24:00 | TERRA_M-M | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 43523367-38e1-34a0-8480-97a48101b4e1 | -22.0825 | -48.47466 | 2024-10-02 01:24:00 | TERRA_M-M | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 705b8570-b1e0-3a7a-af03-788b7107b154 | -21.89846 | -48.4796 | 2024-10-02 01:24:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 9c4274af-0d05-32bb-b7ef-490de65c8640 | -21.88785 | -48.48197 | 2024-10-02 01:24:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 8627f065-a096-3cd0-add5-3ec6e6b7a030 | -21.54965 | -47.78609 | 2024-10-02 01:24:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.7 |
| ae056f44-6aa2-35f4-bbb1-42c7a4aaf7e8 | -21.29073 | -47.62219 | 2024-10-02 01:24:00 | TERRA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 85.0 |
| ba348271-9b28-3042-bcd9-c071629fec04 | -21.28808 | -47.6069 | 2024-10-02 01:24:00 | TERRA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| bfe8077d-b749-3e4b-bfb7-06522c964019 | -21.27934 | -47.62497 | 2024-10-02 01:24:00 | TERRA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 2c324bb2-9f28-3a9b-ba98-a0f25acca175 | -22.39274 | -49.30196 | 2024-10-02 01:24:00 | TERRA_M-M | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.4 |
| 9d733874-ffc7-311a-a096-0cd8d34c92d3 | -22.39072 | -49.28947 | 2024-10-02 01:24:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.2 |
| c3dce7ba-5173-3e74-8472-9da1f7de7d25 | -22.38869 | -49.27698 | 2024-10-02 01:24:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.6 |
| e6880d8a-efb4-3f20-baa8-3562a12d69c8 | -22.38477 | -49.31645 | 2024-10-02 01:24:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 46.6 |
| da731264-b602-30ec-9e35-78949a25f783 | -22.38272 | -49.30381 | 2024-10-02 01:24:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 333.3 |
| 7b922153-7e8f-3204-8179-937a9459c6ea | -22.38067 | -49.29124 | 2024-10-02 01:24:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 153.5 |
| ce79b486-eb11-3bb3-93f1-66a141fd277d | -22.37866 | -49.27889 | 2024-10-02 01:24:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.2 |
| d81d3277-0c75-3791-816c-3ec7d14c2b32 | -22.37268 | -49.30559 | 2024-10-02 01:24:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.5 |
| a661a3da-ebf3-3b0e-8842-c31d8c28a852 | -22.37063 | -49.29306 | 2024-10-02 01:24:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 248.4 |
| f120afc7-d2ef-31d9-8b9f-1dd58f469d55 | -22.3686 | -49.28064 | 2024-10-02 01:24:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.7 |
| cff8dc1e-4e19-3d2e-894c-30ba27c6f88a | -22.36269 | -49.30763 | 2024-10-02 01:24:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.8 |
| d7b81fce-07f3-3777-9918-77a0d5a54ebf | -22.36063 | -49.2951 | 2024-10-02 01:24:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.0 |
| daa08f30-7852-3aeb-ad70-38c9b867a279 | -22.35856 | -49.28249 | 2024-10-02 01:24:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 7e0d3806-c390-3aac-9a8a-8d7207346474 | -22.35678 | -49.33451 | 2024-10-02 01:24:00 | TERRA_M-M | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| 6d6f1274-d98e-3213-8121-074fc710a7f3 | -22.25867 | -49.94815 | 2024-10-02 01:24:00 | TERRA_M-M | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 3f564b9b-4098-3658-b05c-5274e862cc14 | -23.63416 | -49.8897 | 2024-10-02 01:24:00 | TERRA_M-M | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 601fe98e-c840-355e-bd76-d63f146c9b42 | -23.63244 | -49.87857 | 2024-10-02 01:24:00 | TERRA_M-M | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| a5f65a7d-c3be-3493-893f-aae968a43999 | -23.62465 | -49.89153 | 2024-10-02 01:24:00 | TERRA_M-M | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 07fa2834-12e3-3da6-808e-ca1a589759de | -22.40225 | -49.67488 | 2024-10-02 01:24:00 | TERRA_M-M | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| dee79bb9-8347-3ef2-837b-a81ecfc7cd4c | -22.60558 | -48.77907 | 2024-10-02 01:24:00 | TERRA_M-M | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 13.5 |
| aac991b8-c6aa-3d02-81d2-94b2a7c40178 | -22.60339 | -48.76569 | 2024-10-02 01:24:00 | TERRA_M-M | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 90059e1b-1c99-3e8e-bed9-7ca26e780a33 | -25.03405 | -50.72594 | 2024-10-02 01:24:00 | TERRA_M-M | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 9545656f-c230-3d03-abcc-33103304b2ea | -25.03252 | -50.7157 | 2024-10-02 01:24:00 | TERRA_M-M | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 806042ab-461e-359f-aad3-e7e61c16885a | -25.83015 | -50.25995 | 2024-10-02 01:24:00 | TERRA_M-M | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| cb157aa5-0213-3ee0-85b9-f6b066c7f8c9 | -27.04908 | -50.69668 | 2024-10-02 01:24:00 | TERRA_M-M | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| d6a1639a-7829-31b8-8265-34487f38dda4 | -27.0476 | -50.68661 | 2024-10-02 01:24:00 | TERRA_M-M | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 56743bca-04c7-3d9a-b089-f557e42d45cb | -26.95719 | -50.76192 | 2024-10-02 01:24:00 | TERRA_M-M | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 006ec098-5958-3957-8b28-641d90c17bf0 | -19.263 | -50.84413 | 2024-10-02 01:24:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| b55fb5f5-b8df-376e-af83-eb92ddf415eb | -21.64165 | -50.80122 | 2024-10-02 01:24:00 | TERRA_M-M | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 96c7b805-2085-3dab-8abe-cb2fee8a8ebc | -21.64004 | -50.79065 | 2024-10-02 01:24:00 | TERRA_M-M | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 4763aad7-d7fa-3bcd-9a76-7de21fd94a2f | -21.63231 | -50.80291 | 2024-10-02 01:24:00 | TERRA_M-M | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| 39423fac-7556-3db2-9b57-4d88dcf85af4 | -21.6307 | -50.79232 | 2024-10-02 01:24:00 | TERRA_M-M | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| daea85de-5986-3f88-8154-0653deac42a9 | -21.62461 | -50.81532 | 2024-10-02 01:24:00 | TERRA_M-M | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 472dcdcb-647f-326a-b578-813e53da5ea8 | -21.62299 | -50.80467 | 2024-10-02 01:24:00 | TERRA_M-M | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.0 |
| da64b2a4-2952-3f0e-90af-aeb6a8027314 | -21.62136 | -50.79397 | 2024-10-02 01:24:00 | TERRA_M-M | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 6927ceb5-83d8-3258-a449-017d7a951b19 | -21.61366 | -50.80637 | 2024-10-02 01:24:00 | TERRA_M-M | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| 78bfc99f-73aa-3779-a605-844c44c42497 | -21.61202 | -50.79566 | 2024-10-02 01:24:00 | TERRA_M-M | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| aaa25cbf-9873-32e4-a7e8-06cb84c95568 | -21.56806 | -50.75979 | 2024-10-02 01:24:00 | TERRA_M-M | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 9260315a-6e0e-3f35-870b-ddd79762963d | -21.5587 | -50.7615 | 2024-10-02 01:24:00 | TERRA_M-M | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| dc5f5c15-cfc3-3687-9c0f-90430ba22a74 | -21.5541 | -50.76815 | 2024-10-02 01:24:00 | TERRA_M-M | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 9a8ce548-ffee-3d5f-8867-646937d74a60 | -21.55249 | -50.75758 | 2024-10-02 01:24:00 | TERRA_M-M | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 58baa40d-b518-384b-99bc-a5bbb8f1e603 | -21.38184 | -51.03864 | 2024-10-02 01:24:00 | TERRA_M-M | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 980fb1a6-7003-3f31-9203-b86d8539b42c | -21.38025 | -51.02814 | 2024-10-02 01:24:00 | TERRA_M-M | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 43d06f73-28bf-302a-899d-707f08ed01e4 | -21.37258 | -51.0403 | 2024-10-02 01:24:00 | TERRA_M-M | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 5ada8101-42ae-340f-82bd-66fadc61a907 | -21.37099 | -51.02982 | 2024-10-02 01:24:00 | TERRA_M-M | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| e7689bd7-12c9-3d96-ad20-b8780e8828a0 | -23.51356 | -51.10657 | 2024-10-02 01:24:00 | TERRA_M-M | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 36.1 |
| c6bd463b-c666-36c7-aede-9a757ddf70a2 | -26.97391 | -52.04766 | 2024-10-02 01:24:00 | TERRA_M-M | LINDÓIA DO SUL | SANTA CATARINA | Brasil | 4209854 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 3acbd42d-967c-369e-a0e4-63637ba068c4 | -26.75386 | -51.7233 | 2024-10-02 01:24:00 | TERRA_M-M | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| d459215a-3c16-3e81-bbd9-36c52976db5a | -20.09764 | -51.33942 | 2024-10-02 01:24:00 | TERRA_M-M | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4fabe1cd-80dd-36bf-b5cf-b5d99d658df9 | -20.08838 | -51.34105 | 2024-10-02 01:24:00 | TERRA_M-M | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5f5847e3-5ebb-3716-bf95-9b67e21c1dbb | -23.70898 | -52.65536 | 2024-10-02 01:24:00 | TERRA_M-M | CIANORTE | PARANÁ | Brasil | 4105508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 553b1232-60ac-3c08-8438-9dda8aea62bd | -23.70764 | -52.64572 | 2024-10-02 01:24:00 | TERRA_M-M | CIANORTE | PARANÁ | Brasil | 4105508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| ae4f6c12-6de1-3ed7-a7ad-b68609a1ea1b | -22.91724 | -53.11668 | 2024-10-02 01:24:00 | TERRA_M-M | LOANDA | PARANÁ | Brasil | 4113502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 9694be2b-93aa-3fca-add6-0511424c0a14 | -18.89292 | -54.5079 | 2024-10-02 01:24:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1e19b0b2-f935-374e-9f22-fe5152cff030 | -18.88524 | -54.51867 | 2024-10-02 01:24:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 990c2c29-4ca9-35bc-a3b3-d7c0d0566a8e | -18.88397 | -54.50919 | 2024-10-02 01:24:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f0572447-8519-38eb-8dc8-22cf68067724 | -18.8827 | -54.49977 | 2024-10-02 01:24:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4d380e69-dce5-321a-8242-52fa60e1c181 | -18.88143 | -54.49031 | 2024-10-02 01:24:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 07924c3b-4093-37cb-921e-09e44207e59e | -18.87629 | -54.51999 | 2024-10-02 01:24:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0534d4e0-f0d5-30c0-8ab1-798ae2552569 | -18.86623 | -54.51831 | 2024-10-02 01:24:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d6f5dc62-1e2d-34e7-847c-f8fb3780408f | -18.81509 | -54.4777 | 2024-10-02 01:24:00 | TERRA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 09a0b8b7-1351-395f-9eaa-6acc670c6aad | -18.80743 | -54.48854 | 2024-10-02 01:24:00 | TERRA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 08c14914-5446-3337-bfc1-b165c5524ea7 | -18.80614 | -54.47903 | 2024-10-02 01:24:00 | TERRA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1d36e241-8981-3557-9e43-b882858dbc29 | -20.7628 | -54.81939 | 2024-10-02 01:24:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README27.md)
