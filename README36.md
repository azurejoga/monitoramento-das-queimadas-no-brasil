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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f207b43d-d8e2-3551-8867-f5d5d30d6891 | -16.60353 | -58.26235 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 73fe2b06-fd6a-381e-a673-7a4b424b1419 | -16.60933 | -58.22073 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 9b6d3b18-45c0-37c6-a609-023ed820d559 | -16.18735 | -58.4294 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| c6402df2-fe66-30a7-9acd-cc88572d4aa7 | -15.27344 | -58.18404 | 2024-10-02 01:26:00 | TERRA_M-M | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 08368ed8-ba0b-3fb7-a12b-015030abc499 | -14.82581 | -58.61373 | 2024-10-02 01:26:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 1961ab89-2a3a-3e44-9ee7-ade3f92c3dae | -14.82741 | -58.62699 | 2024-10-02 01:26:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bfe002b8-136c-3422-8b77-b76e11677250 | -14.83019 | -58.22061 | 2024-10-02 01:26:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 13d71306-f790-3794-8b7e-9effb077e324 | -18.69919 | -57.32526 | 2024-10-02 01:26:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 238d48bb-e9fe-3468-b1fe-bc58fbdc2073 | -18.72115 | -57.33507 | 2024-10-02 01:26:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| c9c2d498-e99b-3c97-a956-44ab6a8e664a | -18.72267 | -57.34768 | 2024-10-02 01:26:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| b3de5897-9c61-3e16-b9bb-16b0f10072b0 | -16.64775 | -57.2057 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 293b6267-1360-3646-babf-ce45d277ae11 | -16.64923 | -57.21721 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| fc53fd02-f3d1-3fe9-8218-2cf73fde2ecf | -16.64991 | -57.21083 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| b97bd55e-67a7-334d-9958-18fd8f32e6ea | -16.65836 | -57.19795 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.5 |
| b15e1beb-26f2-359c-b56e-8cdc6cb62bec | -16.65978 | -57.20947 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| 95e419c9-6093-3c0a-8afc-320658ef206f | -16.66822 | -57.19659 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 6f0a8d3e-8804-33ff-9e44-99afc46b9caf | -16.66964 | -57.20812 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| c504eaa7-220c-38b7-bd61-1ca77bda45ef | -16.67807 | -57.19525 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| a13ee522-9aa8-3e70-b103-0ba04ffa14e7 | -16.6798 | -57.37274 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 1bc11cdb-c287-3088-9c1c-809fa19101e0 | -16.68649 | -57.1824 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.9 |
| c9569f25-b867-3b00-8924-d4fa5bcccef6 | -16.68688 | -57.34783 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 27d1f4bb-1ec1-3e29-ab75-b7edd931c260 | -16.68793 | -57.1939 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| e9a24ffe-4d58-3c39-bafa-cb4c52e4e7ff | -16.68833 | -57.3596 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| b9827865-b1ed-3429-bbab-a48bcc1fd395 | -16.68978 | -57.37138 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 6d5a65fe-b8b1-345c-abdf-d51bf7374abe | -16.69123 | -57.38319 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 6502880c-3a30-3030-b0b0-6abac76678f5 | -16.69139 | -57.46775 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 79f6d79a-4af3-37f9-b1ba-7fff7a68ea49 | -16.6937 | -57.24009 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 07dac419-1c18-37ff-a25b-fa331edb52cb | -16.69538 | -57.33473 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| aec88e14-c87a-3262-884b-91e3527ff28c | -16.69634 | -57.18105 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| fa367d3c-064d-3c49-8e66-a774f5d72bbe | -16.69683 | -57.34648 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.5 |
| d0bb418e-2880-3818-bc29-010bb53542fc | -16.69779 | -57.19255 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| 67355f96-228a-356d-9f6e-79f22451a63c | -16.71118 | -57.38048 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| ce884649-5fce-3b55-888b-2efa08e0689e | -16.72298 | -57.47564 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 5bcb68e1-391c-3e53-971c-0085bb891180 | -16.7256 | -57.41465 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.1 |
| 430ce4b8-966a-3361-a046-9be2c2fcbb07 | -16.72708 | -57.42654 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.7 |
| 166039e8-9c39-334e-8ad9-7af5a9eaadf0 | -16.72856 | -57.43844 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.9 |
| 01b6c896-cb09-3430-91ef-a28d4aa4a385 | -16.73302 | -57.47427 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 092715bd-3b0c-39d7-8d0a-ce1ba3fc3444 | -16.73709 | -57.42518 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.5 |
| 9ed5e244-3eb7-35be-b97a-b6b4ba0a4723 | -16.73858 | -57.43709 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.4 |
| 2557ccbe-9a78-3a4c-865c-fb9a5cfd6d91 | -16.74112 | -57.37642 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| a9fa85dc-b1c0-3c07-bcdf-cb8937f55fec | -16.74261 | -57.38824 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 8fa5fa5e-5d58-3809-81ab-63bb8231c56d | -16.74456 | -57.4849 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.5 |
| afe3510b-b9e8-305b-a2b9-0b8a4534b110 | -16.7486 | -57.43573 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 6e401d0f-acdb-360b-8ee3-8976b6fd57f1 | -16.75461 | -57.48354 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 888128e5-1553-31c9-a092-260de2540091 | -16.77061 | -57.36666 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.9 |
| ee729010-2417-3461-b6a2-87b1557dbe21 | -16.77206 | -57.37849 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| a53b80ae-f934-357c-aaf6-d6e2bb47bdcd | -16.78059 | -57.3653 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| b2b1ffb8-3798-33f4-860d-957c536093d3 | -16.78659 | -57.49792 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 6978ddd1-d2ae-3f28-befa-c909233e185f | -16.81531 | -57.4818 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.0 |
| 1acf3e10-878f-3007-a8e2-45db3e10642d | -16.81563 | -57.56785 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| fbda8443-5886-3b6d-acde-68859f976d3a | -16.82388 | -57.46843 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 9af60e17-9644-39ae-a0f2-ac1e202c9746 | -16.83393 | -57.46706 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| ea131ec4-cde3-362f-af92-1aecf11f6229 | -16.7637 | -57.80691 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 226a1491-7971-3845-9500-13f5250d3079 | -16.76524 | -57.8195 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| ea3e13b3-5a7d-351e-9800-a89bf2439fd1 | -16.81345 | -57.80735 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 6570b0dc-e9cc-3d70-b2ef-2f2be9b4f2d4 | -16.81509 | -57.80007 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 09e9c953-fc6b-3673-8eb5-d7e9529425f9 | -16.82374 | -57.80598 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| f77a9907-2d00-316f-8314-30d1a3553b32 | -16.83973 | -57.76551 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 32f9e171-0e09-3b6c-8fc6-e8755f9d0444 | -16.84999 | -57.76414 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| c5d24509-c5c3-3852-ae68-3180843ac480 | -16.87146 | -57.68525 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| c6282621-4c86-311d-b165-294786f5f73f | -16.88166 | -57.68388 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| 948ff80e-a39e-3160-bd3a-e273af56b439 | -16.88478 | -57.70872 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 8dcd891c-3242-34d8-b4ef-70a0bc2e3788 | -16.89091 | -57.68894 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 200.4 |
| c28c9b01-6a0b-3d84-b2a1-344186fdc28e | -16.89187 | -57.68252 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| eeb18ea9-ef4b-3e3e-b8f6-014d23cae40c | -16.8924 | -57.70138 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 5e311b8f-5eb6-3bcd-9efb-7f3980eb1b17 | -16.89343 | -57.69493 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 180.2 |
| ef2570d7-21f4-3574-80e5-3dede257107c | -16.89389 | -57.71384 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 1cc1100c-a4c3-363f-b708-ecf030a00a0e | -16.895 | -57.70736 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 231707b8-1ded-30ee-a5de-767a9d345ee3 | -16.89657 | -57.71981 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.3 |
| a2f621b3-e973-3f3e-955b-092276b242f3 | -16.90113 | -57.68756 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| e85695df-aac4-3d3b-9a6d-13ec69a96452 | -16.90262 | -57.7 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 2ebdb50a-5b85-3fd0-aa08-02c7606e9db8 | -16.90412 | -57.71247 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 41460864-2594-32ac-863f-ab96f6e44e50 | -16.90562 | -57.72495 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 8ad6aa2c-0de1-3e81-98bf-534b9d3c3aae | -16.99861 | -57.97151 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 9a7a74c7-dcc7-30e8-8251-26eb6a552a3b | -17.04423 | -56.72068 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 241930c6-c023-3960-a25a-23a2be5a9717 | -17.04565 | -56.73164 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| b90db31b-8912-386b-a0b9-f2c2457ac698 | -17.04707 | -56.74263 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.8 |
| d36db59c-f54e-3588-8cc7-7b93be2af93f | -17.04834 | -56.72555 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| c53589b3-ce18-3e87-969b-d5f89ce30c67 | -17.0485 | -56.75362 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.5 |
| 26224a74-ec54-3fa7-b0b2-8a0b9f3977cc | -17.04992 | -56.76464 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.5 |
| 84004e54-4e6a-3aeb-89d8-f428736e43f8 | -17.05107 | -56.74755 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 22821d15-6f14-34ba-9884-653721a8cb77 | -17.05135 | -56.77567 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 3876a906-a081-3970-8653-4c63c5986900 | -17.05244 | -56.75857 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 578fb258-b80b-3096-88ec-836dc50c557a | -17.05381 | -56.76962 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.6 |
| 3830e6ad-2b3f-386c-888f-b09b6bf56958 | -17.0566 | -56.71323 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 366cdb8d-6c1f-311a-aac8-e6e22b1b9934 | -17.06347 | -56.76826 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.6 |
| 4b81e75c-3e6f-38bf-9282-f8b879d5db98 | -17.06484 | -56.77932 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| ddda2bba-1296-30c9-9fa5-835a3fcc24d3 | -17.06623 | -56.71189 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 516b0d64-6faa-31f8-833d-56ecc376ffe4 | -17.07312 | -56.76691 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 4443955d-4df8-3a18-a810-4898a087783f | -17.08139 | -56.75454 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| f7471494-564f-38fa-a1c0-5ba494ef1d27 | -17.08278 | -56.76557 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.2 |
| ba7438dd-b53f-3b64-bdf6-b8b1e764e374 | -17.09104 | -56.7532 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 3bdc8473-582e-31ff-b0a5-eccda29a6dd8 | -17.09244 | -56.76424 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| cd8cc855-dedc-39dc-a50a-867ea188b25f | -17.10069 | -56.75185 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.1 |
| 5fe037c5-95cf-3930-b895-dd23439bb9f6 | -17.10209 | -56.7629 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.4 |
| b50bb7b5-3791-3024-908f-a477c5b891c5 | -17.10894 | -56.7395 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 7b3a4750-4157-3c1f-8680-c059aca57955 | -17.11034 | -56.75052 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 039bb50a-f9a9-3f56-835c-0849b375ceff | -17.12823 | -56.73684 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 9add027e-3960-3a11-98da-bf9e3b538dd4 | -17.19003 | -57.38259 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 369a2fbf-385b-33d4-977d-362283b9c3ca | -17.19857 | -57.36922 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |


[Clique aqui para ver as próximas entradas](README37.md)
