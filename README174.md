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

## Dados Diários - Página 174

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf780370-52b7-3e7f-b449-f637d54d21a5 | -18.82828 | -42.9896 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1cf5d9bb-68d6-3741-a682-ba53ffd0a361 | -18.82126 | -42.98891 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a6692cbe-4b0e-339d-9105-625618110d72 | -20.27624 | -43.50718 | 2024-10-04 04:59:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d209c085-6674-356d-aa20-27ab656207ae | -20.27505 | -43.52301 | 2024-10-04 04:59:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7f6d4a24-a781-3631-8cf6-5a2bddc8f473 | -20.27493 | -43.52133 | 2024-10-04 04:59:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 023970da-4de7-3afa-8e8d-e125d7615fd6 | -20.26838 | -43.51916 | 2024-10-04 04:59:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 923696cb-02cf-38b0-97d8-66dda6279b74 | -20.26742 | -43.52808 | 2024-10-04 04:59:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b735de85-e71b-3951-876a-eb466c8f7c27 | -20.07966 | -43.44161 | 2024-10-04 04:59:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2ded5722-a0a3-3213-b686-2ac2da369e33 | -20.07947 | -43.44373 | 2024-10-04 04:59:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 15765d78-0955-3a60-854d-9a8faa9af22e | -20.24511 | -43.19138 | 2024-10-04 04:59:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 62562e30-4fec-3b5e-8bc7-71b2d7909021 | -20.23859 | -43.1841 | 2024-10-04 04:59:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dcca0d73-d5ce-387d-88d5-b6d476ad0ef5 | -19.51082 | -42.89169 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4263cffd-e9dd-33f1-bd36-b1146eb4332e | -19.51031 | -42.89829 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1b2678de-3a5b-301b-a326-ebaa3dc9cb6d | -19.5096 | -42.90747 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 07a4250b-99ef-3e43-9722-bee4a69b6564 | -19.5089 | -42.91645 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 53d79358-58d8-3ef6-b587-c5760257d2b2 | -19.50838 | -42.9232 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ee7f5692-80c8-3d29-8e0e-ea0b94c33522 | -19.50764 | -42.87829 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d1dcf3ab-d0b5-361d-97a6-fc7c3bac8f30 | -19.50702 | -42.88582 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9372df20-ddc7-3ea9-9eb1-02bcc2c6c4b0 | -19.50653 | -42.89169 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 28b4a800-40d1-3d60-8973-a178998dcbc6 | -19.50604 | -42.89754 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4ff3c557-d3e2-3860-b3a9-cda0ff674a48 | -19.50594 | -42.86218 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 652881ce-3b9d-365b-a3f2-00fc964313b6 | -19.50541 | -42.90512 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b353de9d-77cb-3911-b3a4-1db315e03d4f | -19.50533 | -42.87002 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 2bfd5449-7465-334b-beda-44cf42de51c2 | -19.50456 | -42.91524 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a13a1ad6-5fdd-3e09-be10-47575feb7e86 | -19.50454 | -42.88033 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 252a40b7-363b-3404-8684-e363ca779554 | -19.50401 | -42.92176 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6499a22f-7b51-3fe7-8eee-5c2d3f59dd23 | -19.50399 | -42.88754 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.5 |
| ba0f8069-c986-392c-a081-7c19b7dc3aca | -19.50358 | -42.89283 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.5 |
| 327b362a-75d4-3ee2-8122-396ad8ad867a | -19.50346 | -42.92843 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 94cd1b7d-b0be-3fb8-9e59-fca8b70446eb | -19.50314 | -42.89854 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.2 |
| 2b2f38de-ecc1-3966-ba60-58e76635623d | -19.50254 | -42.90626 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.2 |
| 82ef98f5-12f5-3bf3-b9da-a7b8badbbd5e | -19.50189 | -42.86135 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 09079b95-c066-38ae-ac8b-10b9d8a45582 | -19.5018 | -42.91593 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f9679f4d-8b9d-353c-90b1-157ade932577 | -19.50127 | -42.86891 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| ab24fff3-bffe-3b5e-91da-d3eed619682d | -19.50126 | -42.9229 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1760c853-163c-312b-849d-5eed00446a37 | -19.50075 | -42.92951 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ab4cf302-869c-3b11-892f-2ed3d2d7f099 | -19.50033 | -42.8802 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| d9a2f60f-870e-3e8b-bd07-27e9ebca55d9 | -19.49977 | -42.88684 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| 68575ecf-f6e8-3ba9-93d6-6c5d305928a0 | -19.49935 | -42.89203 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 274.3 |
| 2e49b7ac-3e11-3660-9e22-b6b37a97c8ba | -19.49927 | -42.85574 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 686f0f78-01a2-3dfa-a0df-b48e92db60b5 | -19.49891 | -42.89734 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 274.3 |
| e36fb71c-2497-34e5-b1fd-e7f826a5d02c | -19.49874 | -42.86269 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1b70d39c-04ef-3f0f-b899-1326165a8adc | -19.49835 | -42.90409 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| c9b20d14-803b-3bd5-8aa5-5f3897e949c7 | -19.4982 | -42.86976 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| ed3d3deb-000e-3048-9927-ba1b106968fc | -19.47886 | -42.88018 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0e7982e7-f13d-3229-a8c1-1aa9416bebfd | -19.47834 | -42.88661 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1cfc01d2-7692-31d7-b439-3d2ae29cb9b1 | -19.47786 | -42.89244 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e2927736-c78d-390e-9fac-89972313db75 | -19.47737 | -42.89844 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c86ec022-a940-3c95-a3d8-06ed0a6e9197 | -19.47685 | -42.90481 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 05f23e49-9263-3ed0-94ec-d25c5249f277 | -19.47544 | -42.88681 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 43626985-cd38-3402-a142-a02048ee02ba | -19.47499 | -42.89278 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6481f82a-9dee-3e75-9958-4fc5a1f033e7 | -19.47131 | -42.88504 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 71acc544-255b-32e5-a928-89b4ce877f98 | -19.4708 | -42.89137 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9adeff79-139c-3ccd-a9c5-48b301f79c2d | -19.44156 | -43.07542 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 06b89ee9-321b-3408-ab74-13e2702b9e19 | -19.44107 | -43.08139 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 47d1a6d7-45fb-3e59-8241-e19103d1c9a2 | -19.44062 | -43.08696 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e9b62f41-18cc-32ec-b042-3602f37db7e7 | -19.43984 | -43.07586 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4bf46e06-0f8c-3521-ba5d-7a3d303d4b8c | -19.43939 | -43.08178 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a8272c1b-ffd0-39da-aa9f-268622a0684e | -19.49753 | -42.91387 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| a6abbe10-d4db-352d-a668-eac5373b73e5 | -19.49727 | -42.88191 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| b1c335db-7ade-3c52-b67a-186905808463 | -19.49683 | -42.92226 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6476ccb7-85ff-381b-b636-ec3fc8be01f9 | -19.49683 | -42.88768 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.5 |
| 0d2b3da5-37dd-3b28-b6ca-50224b74915b | -19.49629 | -42.92877 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 47249ca7-43e2-3ef0-adc4-763063f1210a | -19.49603 | -42.89809 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.2 |
| 564271fc-d62f-336a-8c73-c181ecf5129a | -19.4958 | -42.93464 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 57673874-c0b4-383d-8089-e096127c3f79 | -19.49577 | -42.84872 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 830a6d12-42a7-3e29-a657-7accd0eba43a | -19.4955 | -42.90488 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.2 |
| ce4c0aad-6ac8-30b8-a49e-c10fed8b89bb | -19.49523 | -42.85524 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 15736b21-ef5e-3052-b698-34c7d42a19fa | -19.49476 | -42.91457 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e5772541-796d-37cf-a0ea-4c6b5408d58e | -19.49463 | -42.86253 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| f533a290-07e2-3225-acfa-1163e18dfbb2 | -19.49413 | -42.92284 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5cbbc6cb-494b-3640-9ddd-eda261f36c0a | -19.49405 | -42.8695 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| eabfb0f4-ef58-38c3-96d1-ffe916e2c667 | -19.49362 | -42.92939 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7c151f21-93cb-3265-aa6a-13838757ad09 | -19.49318 | -42.93521 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f086cc21-b870-3659-a09c-9a63b56e07cc | -19.49308 | -42.88124 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| 48061524-8b7b-3d35-9ba4-d066c6b38123 | -19.4926 | -42.88706 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| 06e8772e-5a95-3ab1-bceb-71921adf7ae8 | -19.49202 | -42.85686 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 59b5effd-1180-3fa6-94be-c5492c14bd0b | -19.49177 | -42.89723 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 274.3 |
| 7d86b48b-2588-3deb-a222-e9b81cefa6ed | -19.49144 | -42.86449 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| e4a74e31-72b1-37fc-97f1-c1517d283c5c | -19.49125 | -42.90354 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 4bb36a99-77a3-314b-8a5f-b0f894715994 | -19.4909 | -42.87157 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 00aee9f0-36d2-3ea8-9631-eaec56bde4b2 | -19.49051 | -42.91239 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 2904b682-6cdd-38e8-9a41-66437dcd8447 | -19.49011 | -42.88203 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 03220595-a666-31d0-ae2e-2dba6bbf1ace | -19.48984 | -42.92051 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fbdb316d-4d0d-3a45-86be-74f8b536811c | -19.48966 | -42.88787 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 184.0 |
| aff8804e-dffa-3cc4-af61-e18d42f24dcc | -19.48925 | -42.92761 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 795f7720-1e7f-3eee-9a9d-52bec1dacd63 | -19.48888 | -42.89801 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.1 |
| a4a65437-3e30-3d56-8746-aeb42c072ed3 | -19.48874 | -42.93377 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7e1c6de9-e3ec-33a4-ad18-4dfb4201c2bc | -19.48838 | -42.90458 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.1 |
| 7aed36a7-ba8d-3f3f-bbbc-9b7c15c7e5d8 | -19.48824 | -42.93987 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d7c5bf41-9a6f-3b39-bc46-90f423069cc6 | -19.48794 | -42.85671 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 279eba39-86b9-39f0-9b3b-16e0aad1a48f | -19.48773 | -42.91311 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5271a3a6-69da-31d1-ac9c-87c91b514901 | -19.48728 | -42.86483 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 6daa069c-b34e-373c-9199-76a6743486b6 | -19.48715 | -42.92079 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e126d475-dc92-30ae-a5db-458266039d7f | -19.48675 | -42.87124 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 0f28fac6-bd70-3695-b767-c4e2ccb316ae | -19.48659 | -42.92806 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 48e437fb-691c-3284-8511-c9aedb1081fe | -19.48611 | -42.93429 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 47b9f325-149c-3b5b-aa67-c6858639122d | -19.48596 | -42.88089 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7b02891f-42d0-375e-9955-53025c804166 | -19.48544 | -42.88718 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a9e30276-b123-348d-b4a7-0feab5750896 | -19.48502 | -42.89232 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |


[Clique aqui para ver as próximas entradas](README175.md)
