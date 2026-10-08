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

## Dados Diários - Página 195

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02a448c5-b616-317c-8f99-027183ad59bc | -2.99827 | -54.05027 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 626b85db-307d-3444-aefe-5d1856ce4b5b | -3.74207 | -59.44982 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 972a7b5e-83d0-35ff-a6b3-65ad50779402 | -3.35084 | -59.50572 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7c378b2-a1dd-39c9-988e-e838ed912364 | -3.32976 | -58.16376 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef9cd137-730d-360d-ad9c-e62280003d5c | -2.67075 | -59.91436 | 2026-10-08 05:42:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 067308de-7f31-30aa-8b86-b53e52d126bf | -3.03904 | -59.11504 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b566211b-1214-3984-a2d5-a78033365694 | -4.1408 | -54.92572 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74ff1998-2fa3-3341-83f3-eb7a91cbf3ce | -6.6194 | -59.9425 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3539a4c-1063-3452-a11f-9ea34584c18d | -3.28545 | -54.03866 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23aa8801-d340-3d6c-bc74-3ca0222ea8fb | -3.60194 | -54.56975 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 574a85ef-dee2-310a-a630-2c26b8b503b6 | -3.6795 | -60.59156 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67d3917f-57eb-35df-9c9f-3d05cee39066 | -3.26307 | -54.04199 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c8a85b7-efb6-3bd1-b082-10300aa4e684 | -3.01299 | -54.13324 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0eb19b29-fdf3-32f3-8bf3-2f18ba2873df | -6.99027 | -59.10507 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed89f48c-812e-3ae6-86e0-a81f989f0a83 | -3.96521 | -56.128 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fe20e66-d34a-3d80-9ce6-8c8bf2838c94 | -3.28493 | -54.04203 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d81f9e3-83d0-31f2-9f23-4f753259b441 | -2.78566 | -54.07415 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c2a9c45-35f7-34be-917a-b9dae5c439eb | -3.08286 | -53.96052 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 07ea1686-4c71-3377-985d-b724923653b9 | -3.29818 | -61.01275 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e854403c-1ef4-3289-9b5b-59e8982b460b | -3.58289 | -54.66148 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e579a10-83f9-3c70-9b40-3dcb62a40f9b | -3.26324 | -54.67844 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 720bbb0d-5f5c-3228-addf-90a774057208 | -3.59537 | -54.5782 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97c75fe2-00b4-3cad-b54c-380dad28bc00 | -3.5488 | -54.67844 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0d9e8353-7fae-3097-b10c-02bca9891e73 | -4.74963 | -55.65374 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| feb063c9-1d82-30d6-9b80-9215a1b4927a | -2.99524 | -54.10706 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72439fa6-4688-3645-8476-d7eede3d747d | -3.02391 | -53.95156 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 225cd8aa-daa8-3130-bb2d-9423b1b258ba | -3.00831 | -54.09225 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 52e40d5a-385a-344d-9e6d-f49dbcb349ee | -3.31795 | -58.26947 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8382b7c-445d-3889-a54b-2aecd486067c | -3.03513 | -53.94989 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f827d7e-5e43-3020-acde-a0bbc929b9c0 | -3.84802 | -55.98575 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f64ba511-05d4-3638-a91d-be854a444342 | -2.93394 | -54.05312 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88deffb9-07b0-3d08-9dc3-58d3ac35bf72 | -3.31091 | -53.87224 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 77cbd2a0-b7d9-37e5-8587-ef541f954b67 | -4.07064 | -59.83568 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 878c206a-3592-3951-9ccd-5724258818f0 | -3.18425 | -60.05423 | 2026-10-08 05:42:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5cc6928-c96c-343e-a051-48c219ef16f4 | -3.04557 | -53.91692 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 082e3bb9-da0e-3b55-b7ab-36f9ec4a9a03 | -3.57416 | -59.46259 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfd74c1f-3e30-3e33-83c6-ae523f084bd1 | -3.29472 | -61.01223 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4b1af2cb-1d08-38d4-9144-ca40d5104156 | -3.30506 | -54.03823 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44662854-28de-3eb4-b01f-3a09b69d9938 | -4.30891 | -60.94654 | 2026-10-08 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97793c72-f314-326f-b974-8e05b3206f27 | -3.54319 | -54.68087 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 21fe7d0f-271c-35dc-a21e-8f9a232c749f | -3.51967 | -54.66198 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9efa31f1-c295-36e6-b284-ee3658599ce5 | -3.01794 | -54.10041 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f074baa-a952-31f9-bbb9-351fe6bfe381 | -3.51738 | -59.32692 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b5c98ae-f5e1-38c1-9008-fe0fa25fd92a | -3.08052 | -54.28928 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 372b4f05-eed6-3711-8ad6-f53251b915aa | -3.08053 | -54.25327 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 297a5c28-0251-36c2-8dde-3c8e0e953fb0 | -3.0753 | -54.28838 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2263ab7-2f21-31d8-ba7a-1a4e787d1d35 | -7.39124 | -55.20153 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c76903d-95d3-347a-b20c-221111d86721 | -4.56501 | -54.9596 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31256d04-52a7-383e-bbfd-da87f29a87a7 | -3.06173 | -59.27079 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 933e2fb7-2c00-3026-b4ec-97dd9010d86b | -3.44727 | -59.82933 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8266b81d-546c-3d77-ae19-4a9d75c4a2d4 | -3.2123 | -57.86993 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11a57b07-83da-392e-b86e-b4eb6b4e40c0 | -5.2334 | -56.1145 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68c677ae-f5c9-37f9-a56a-c7e2c27afe74 | -7.22931 | -55.17133 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 904ea963-8c06-38bd-8034-e3020c6b3bd4 | -3.29104 | -54.07347 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55d44d08-0fc8-3f82-9afa-f0150254b998 | -3.73928 | -59.46778 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ec1ba07-4010-3e10-9033-1ef01e4e3139 | -2.80105 | -54.07981 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa881c9e-d8ea-318d-8e74-df641869d1c6 | -2.48416 | -56.13401 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fbf74ed7-7403-3a40-a0e6-46ba32446884 | -2.88544 | -54.12309 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a5e88b6-f831-3480-aca4-2024d3c1ab08 | -6.51298 | -55.38443 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52bb210d-9636-3439-9f78-113e82c4883e | -7.21958 | -55.09121 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9240033f-57d5-3de6-beb1-d84b4e5f0d77 | -3.03128 | -53.939 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d7ab5df-c877-3600-a15c-93918bebbca8 | -3.08338 | -54.306 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2dafcee6-b1d9-3b56-8d05-e13d164d34dc | -3.29494 | -54.01246 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13d79c73-ef36-37da-aebb-b1103867aa9a | -2.99484 | -54.07338 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9b6af576-4856-3641-83cd-8e528a81ca7a | -4.26539 | -54.87763 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cf8135f-ad7e-3a97-8da4-2c7ac8e975a5 | -2.48661 | -56.14858 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d11cb92f-dec5-3d6d-8517-59c70ffd6b6d | -3.29358 | -54.05696 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c69986b-58af-33c9-9cbb-2ab7e1673cae | -6.52328 | -55.27668 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d11cc45a-02d9-3696-be5c-dc27f89b1457 | -2.89676 | -56.675 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4c8e650-c778-3830-b9a5-416a0dee6402 | -3.28772 | -54.05953 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d41faf1-1047-37e6-a0d7-86bab0f4898c | -2.9832 | -54.1152 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8745e005-7246-3f88-8339-6c0ca9102122 | -2.7755 | -54.10585 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c0e79dd-e58c-30d3-91e7-785a3f7b761a | -3.6308 | -55.50945 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00ab3de4-7e66-39a8-9750-65225130e7d2 | -3.59743 | -54.66985 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d6198a0-e251-3184-a323-b7daf35fc7ed | -3.51159 | -54.66541 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21200841-253f-332c-aecc-ab5b5e6a0f7b | -3.27503 | -54.07107 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b233a64f-4fbe-3158-a048-9cb8b2f057e8 | -3.74162 | -59.47733 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df8971c3-2313-33a4-a60b-566804b3859e | -5.28438 | -60.08997 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf32e307-00fa-3417-9fe7-3d5e7d41f2ec | -3.99766 | -56.26198 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5999ed30-99ed-355f-9c17-e7fe9425ee46 | -4.92427 | -55.85876 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7609f26f-40be-3ea8-bf9d-d8b4e4ebc1d4 | -3.29002 | -54.0801 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c47824b-74b9-3742-bf4b-83795760bcab | -3.21828 | -54.30187 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92fb7896-caee-35da-9623-f5ae8c90d42c | -3.50355 | -59.94917 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a2b13f9-86d2-3512-9cd4-6fef987f8f8d | -3.02711 | -53.89332 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d1d4c4c-c833-3ebc-8415-3ac938aca00c | -3.30187 | -61.34472 | 2026-10-08 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f13f1ee-2486-3365-9ab2-96f871fce248 | -2.87334 | -54.20392 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 41c20e0f-1146-3648-94db-558eecfe9cc4 | -3.04705 | -54.15829 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a000d645-5dd7-3dbc-81bd-e1d74dc68663 | -3.25973 | -54.02793 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 56ed0340-d537-3984-8277-39a084c42d79 | -4.09788 | -52.07425 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29848209-a6a5-3400-b6e8-dfe683a78807 | -3.00015 | -54.07418 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 498a7f84-6a12-3f3d-9734-4099fede3370 | -3.30942 | -54.04578 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93ac5aa6-4ab6-338b-8f29-3c0e43a63bad | -2.49286 | -56.16878 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 08583dd6-e12c-3e34-a0e7-014da656b803 | -3.13349 | -54.36813 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f9a01c00-cafb-3641-beca-925a41767b02 | -3.29385 | -54.07751 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b965faf5-91f0-3317-8708-ee35ba39a205 | -3.58435 | -54.68684 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b441e9c1-c536-3d86-9e06-8e16e4953cca | -3.47741 | -59.58596 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 67193c3b-34c1-33b0-9ab9-c016c4283a09 | -6.23944 | -52.8563 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 393f338c-4fc4-3f96-9c8c-cdea2d39b78a | -3.81414 | -60.47237 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2d70238-0c35-3400-9f6d-5f3951da099a | -2.89601 | -56.67308 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3bcfa94d-e6ff-3192-9df2-6120329f1f9d | -3.54454 | -54.67168 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README196.md)
