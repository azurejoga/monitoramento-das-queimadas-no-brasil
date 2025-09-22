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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e61ec27b-a618-3698-8d13-2a3a82af0aea | -15.00923 | -55.31189 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cefcd69-5ab9-3d32-ad84-9c66a9d96ae5 | -11.63215 | -52.84839 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 28844a16-1fe0-3d6c-87ad-9a40f4603f85 | -17.35985 | -46.814 | 2025-09-22 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 324d224e-4b53-3b3e-8f3f-0bf0dec415fb | -13.31835 | -47.29406 | 2025-09-22 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff1d245f-cc2b-3b9f-a119-f47f6c5429e7 | -11.66118 | -47.49543 | 2025-09-22 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae571c69-ebbe-343a-86e1-9141a4b73a6b | -11.41157 | -54.72 | 2025-09-22 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48e3a164-b631-3f71-8cb9-1bd253bea050 | -12.85831 | -52.99219 | 2025-09-22 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a2ffc0a-ccaf-3fb6-8054-26a5a64771dd | -11.70203 | -41.49656 | 2025-09-22 04:40:00 | NOAA-20 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 51361e49-3f87-353b-b434-1a0cfd8271c9 | -10.62593 | -51.58393 | 2025-09-22 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee7f3852-ed96-32ba-9412-1e1d9aa2cca7 | -16.00157 | -59.45145 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8350f21f-1f97-3af9-a794-181c1baaa687 | -13.27145 | -47.64293 | 2025-09-22 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a7fb7e9-884e-366f-be63-faaa58a9a37a | -10.71442 | -52.47819 | 2025-09-22 04:40:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e09bc784-8c74-32f3-ab64-6360bd39bcd9 | -15.0328 | -55.28745 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25b4f8cd-53dc-356e-9044-41f1f5e64a8e | -11.46272 | -43.53501 | 2025-09-22 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b30106b2-8cfa-3002-ac0a-6f9348ba9019 | -18.40074 | -42.85693 | 2025-09-22 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f3953b27-e4b4-33be-b1d2-e3533b13cd1d | -17.27244 | -43.44639 | 2025-09-22 04:40:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd152575-3c39-3e8b-869f-05885ad4edb7 | -11.7351 | -47.79964 | 2025-09-22 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 16ec294b-0ba7-3e01-b683-4f2dbe61f47d | -18.84874 | -42.19663 | 2025-09-22 04:40:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6e966c5d-bccd-39c2-9dd9-fe6e2a1a869e | -14.39644 | -48.55367 | 2025-09-22 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4335fe04-079d-3e86-a7c6-ea3e2ac99df1 | -11.32402 | -54.34586 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8bb17baa-425f-3a06-9692-f240e01e60c6 | -14.61707 | -49.75124 | 2025-09-22 04:40:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8212e995-86d9-3e26-8b85-2dceb362ade9 | -15.82495 | -59.59225 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8db8d581-6dd8-3e25-9ae9-670390f5d086 | -17.44419 | -44.81721 | 2025-09-22 04:40:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 983810c8-bc4e-3c88-b65b-cd910d7c6d29 | -17.10438 | -45.91056 | 2025-09-22 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06830773-a6fe-3730-96e1-7f3a9867c1ee | -12.06361 | -44.82607 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0d7b813-fd2b-3343-9a7f-85dfca535eb8 | -12.06625 | -44.83867 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1eb5c3ac-d72f-33f2-a02d-a3b554b313c2 | -18.40165 | -42.85711 | 2025-09-22 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fc0bc5c0-d57e-34eb-89a8-3e9ae76ce068 | -18.40041 | -42.86005 | 2025-09-22 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bf5ac79e-5071-37f1-bc93-ce53e8ef0f13 | -15.09532 | -43.84166 | 2025-09-22 04:40:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d4b1995-31b0-35e1-a47a-def484db2b02 | -17.05107 | -44.90712 | 2025-09-22 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf275c5a-4a63-39d8-924f-273134da44cd | -11.32697 | -54.35112 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41d38374-38dd-342a-96f9-35f765cd93c1 | -10.40144 | -54.31484 | 2025-09-22 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 339f11a7-0050-392a-a317-743863c85008 | -11.61259 | -54.65882 | 2025-09-22 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ece0470-872e-3207-8966-cb27a9a6fb0f | -18.8429 | -42.1988 | 2025-09-22 04:40:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4a0bc4c4-9d31-3305-aac8-a0741d61a7ca | -11.44888 | -43.53613 | 2025-09-22 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75c0b7c5-0896-3a96-9001-3c8df89f4686 | -14.69093 | -48.78457 | 2025-09-22 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cfd7f12-667a-3789-ae5e-f5a2a764109c | -15.29739 | -56.80201 | 2025-09-22 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e3a90fe-e7a1-3384-8433-6fc9ca7f0462 | -13.30662 | -47.29672 | 2025-09-22 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8df6869-7483-3750-bfc3-47933fde4155 | -11.3203 | -54.34518 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba851022-947f-3ee7-b589-2706011bd6bc | -15.04397 | -55.2896 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 897c8d14-e22f-386a-b2b4-2ca17498f8ba | -12.71464 | -47.69467 | 2025-09-22 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7bb43e5c-5d37-3ec0-b076-b10baf61cc27 | -14.61077 | -56.03005 | 2025-09-22 04:40:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16a4f24c-c7c1-3220-803b-868e7d06e91c | -13.23828 | -47.21821 | 2025-09-22 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4ebf757-d7ed-3ee1-a049-fa5924d23b28 | -11.31285 | -54.3438 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed7e4f05-c06d-346a-a1b5-4519560e0736 | -16.00321 | -59.46835 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 47c18afe-f2e2-3fb4-9795-27441a1bf9b2 | -12.6855 | -46.83924 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd85cbd0-b0be-358a-a273-6a0ae6448444 | -13.86349 | -44.19986 | 2025-09-22 04:40:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2595068f-737d-3d10-a57f-6670eb806529 | -15.7709 | -59.41699 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cd9c4aaf-798f-332e-84e4-7454f99a83f0 | -15.95133 | -59.3783 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be363281-0650-3191-a6e5-6d42074a2e78 | -17.10066 | -45.90588 | 2025-09-22 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae6082c9-55ab-38e3-8c23-c4e0093dc619 | -11.65821 | -47.4907 | 2025-09-22 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0a8f620-7cec-33d3-810c-35a0f2e4735e | -11.70161 | -41.49987 | 2025-09-22 04:40:00 | NOAA-20 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 43e2b41a-64e5-3193-9c30-40d078fe67b5 | -11.46856 | -51.48302 | 2025-09-22 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3552e52-286f-3178-b820-366a3b53dace | -11.265 | -47.48222 | 2025-09-22 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06e56897-dfeb-38a8-8346-51c525d9886c | -13.31401 | -47.2979 | 2025-09-22 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4eae4ca0-6dcf-3d0e-a5f5-7365deb50a85 | -17.4324 | -44.79852 | 2025-09-22 04:40:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bbdc251-3c10-3c39-96b0-7579967daa24 | -11.87806 | -64.94496 | 2025-09-22 04:40:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ba51b57-0c0c-37d9-89e6-42d90070e1ab | -15.03941 | -55.29365 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 978e210a-34ad-3dd0-a11b-01d0ea8835ed | -14.97735 | -44.41979 | 2025-09-22 04:40:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee9db01e-ba54-30c9-ac3f-654a6e0b63d2 | -11.2549 | -51.48082 | 2025-09-22 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae9bdf8e-7ffa-3104-a15d-d6d4b1914a52 | -18.37569 | -43.70179 | 2025-09-22 04:40:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ac270d5a-0273-3943-9518-debf22532118 | -10.86824 | -52.07655 | 2025-09-22 04:40:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b2ac6e1-7fbb-3144-ac0d-2629df9c39ad | -11.8628 | -45.21812 | 2025-09-22 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a104a2a6-caa7-3b55-bba5-7a6a6341596d | -15.76673 | -59.41351 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7093e4a1-1390-32fa-ae99-ea49da342015 | -15.77387 | -58.69934 | 2025-09-22 04:40:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1161e843-0747-3355-9a58-4c5c34c37401 | -11.79114 | -64.93301 | 2025-09-22 04:40:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d562a269-8252-3b39-b572-acb7f90b3356 | -11.31734 | -54.33995 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7066355a-d1dd-398f-833d-2cec81f5e8ed | -14.58546 | -56.03585 | 2025-09-22 04:40:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07538a5d-58fc-3bbf-b877-d72698e69261 | -11.63995 | -44.33483 | 2025-09-22 04:40:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a937c66-793b-36c8-b5bc-7e0f2b66eee8 | -12.70156 | -46.86146 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07a54d41-dc76-395e-bae3-4e40bcbe7ed8 | -11.46333 | -43.53302 | 2025-09-22 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccc4c559-5ccc-3264-b56e-0608c8e4a111 | -12.21502 | -47.15702 | 2025-09-22 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb66ad97-2f21-3cb3-9cfc-96bf2e1d36bc | -15.09595 | -43.83647 | 2025-09-22 04:40:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 883b7bff-2363-3514-b3b5-d622927b58e0 | -15.7739 | -58.69851 | 2025-09-22 04:40:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bf7efe39-9ca5-314d-b978-8a0dc24c0771 | -15.28688 | -59.41653 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 100e3c75-f29b-30d4-8777-ef1c8bef4fd2 | -15.03362 | -55.28278 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 336e4da8-a821-39aa-9ce1-5fda0c077693 | -11.8623 | -64.94897 | 2025-09-22 04:40:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e74527f6-33b0-33a0-9ed0-2c4e0dd0d777 | -15.05297 | -55.28217 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5086295f-c0f7-39b6-b592-90ac12468ecc | -14.0785 | -50.15393 | 2025-09-22 04:40:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08c20eb0-58bd-3478-ac16-001f7c84438b | -13.24198 | -47.21887 | 2025-09-22 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fafdc7c6-3761-301d-8569-849f03194975 | -15.76623 | -59.41554 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ffd94a88-afba-3cd1-8d72-7a9e925e0906 | -14.39996 | -48.55424 | 2025-09-22 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9149e6d0-4b4b-3714-9a44-2798e4760c3e | -14.77132 | -48.60653 | 2025-09-22 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a0be56d-85e2-365a-aaa7-0789d171c7cb | -15.83147 | -59.59224 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03be5da2-5eb0-3728-bce2-8a54427276fa | -12.07048 | -44.83931 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bfe2a10-1b46-3b36-8451-78246e9d7485 | -11.50025 | -43.56963 | 2025-09-22 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e598bed-423d-3e42-ada2-e98a418aa2fa | -10.45904 | -48.23202 | 2025-09-22 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72ba4841-b716-38c9-a48b-6d50eb555a8c | -15.93928 | -59.41524 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48ad10e1-4b2c-359c-8e5c-6582c5640067 | -16.00796 | -59.46935 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d99cc321-d54a-33ce-ae36-634fb6e89174 | -12.6971 | -46.8657 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbb2b8ef-4a49-3130-b12d-f26020f888b5 | -14.40348 | -48.5548 | 2025-09-22 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3318376d-ee3f-30fd-9091-cbe98ecc2973 | -11.7336 | -47.80577 | 2025-09-22 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f81bd0f5-61a9-321f-887f-2d855425e39f | -15.1595 | -49.58469 | 2025-09-22 04:40:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8283f104-d253-36c7-a301-272b3c0ad91b | -12.68926 | -46.83983 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29f9396c-d5e2-3962-a824-e1f75cbc65aa | -11.63779 | -52.85728 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 691992a7-064d-3673-8d43-0b6251d5d5a9 | -18.35952 | -43.71041 | 2025-09-22 04:40:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18ba1577-fbdb-3d36-9509-5e6377cf6480 | -11.73715 | -47.80632 | 2025-09-22 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d9bf5b1-dbdb-3c04-b770-8f81e68e0e33 | -11.42848 | -55.01166 | 2025-09-22 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb03f794-ee07-39f6-94b2-9b8ef5959e25 | -11.77851 | -43.7625 | 2025-09-22 04:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 86b61021-453f-3ec3-a662-bfe540d29bb0 | -15.87051 | -47.28516 | 2025-09-22 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README32.md)
