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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 041faace-7eb6-33df-ad1e-64ff654d899f | -7.38832 | -59.72025 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3307acd2-dbfd-3f26-91e0-daa7fc9b0102 | -7.38775 | -59.7223 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e29ab3c8-5252-34eb-b7d4-b1f6e05175f0 | -7.38756 | -59.72477 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c55d294-a938-3083-a44c-6abee96da57a | -7.04337 | -59.26451 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 22919826-7fad-39cb-bba3-82a936cb61a2 | -6.79125 | -59.35344 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a8b5bf6-edd8-311e-a279-aa5443a838d3 | -6.79053 | -59.35785 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3aaceb7f-0353-3712-bf00-461a6fb45797 | -6.78754 | -59.35279 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 453ae9bc-2c98-314d-a47e-cac62988c12f | -6.78683 | -59.35719 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f940d3f5-bb15-30e3-93a7-e6a9541d587b | -6.7489 | -59.33279 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7aa1f158-80b8-370e-b9bf-110191bb62bf | -6.74818 | -59.33718 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5598dbb-b766-3f44-8cec-7a09d4ace2b0 | -6.74592 | -59.32775 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3f73432-e6ca-3b57-bc4b-21822319a87a | -6.74519 | -59.33216 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bc1f40d-c2b9-3328-9c78-450c35e55769 | -6.74447 | -59.33656 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8ec9d55-51b0-362e-9f70-1a67fed66aa1 | -6.74221 | -59.32718 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2808abae-ee8f-38c2-84de-4c313b4b2e2d | -6.67316 | -59.48725 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77b3adc9-a270-3582-829e-6ee27552ec34 | -6.67307 | -59.48941 | 2024-10-13 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cde430fd-7921-3767-9504-343f867fe90e | -9.23033 | -59.74899 | 2024-10-13 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bbecaeb-b363-3c18-b138-5e1688590b62 | -9.21134 | -59.77255 | 2024-10-13 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc657730-80b7-3c0e-aabf-2e5e1e591bb4 | -9.20909 | -59.76325 | 2024-10-13 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aadfdf78-ad81-32f6-97ff-619afad882c8 | -9.20838 | -59.7676 | 2024-10-13 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5181fa0-c05f-3830-b671-84b924bdd0b9 | -9.20766 | -59.77195 | 2024-10-13 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e72f358a-8b6f-32c8-b3a1-1358e1afd6d6 | -9.8587 | -60.11533 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8e5c069-343c-345f-9b97-c2b6da043b23 | -9.85222 | -60.31379 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63fc869e-f497-3333-8980-a828b76593c0 | -9.85145 | -60.31841 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03a8028a-a2c6-3594-b8b5-c064c8f65e4b | -9.84846 | -60.31317 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab631b7d-96df-3e0c-9708-407e8d9f903d | -9.84769 | -60.31776 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a2c9d49-f5e6-3ea4-b52c-cb3be569c4aa | -9.8447 | -60.31252 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0d6cb2f-e85e-3cc0-b567-eaa0a7889fd2 | -9.84393 | -60.31711 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0728cc5-3471-3f87-af73-8a17224bddc1 | -9.84316 | -60.32168 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2c4e2b05-3574-3fc5-a39f-dfb406803dda | -9.84172 | -60.30726 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 715981a4-d796-3bd7-a6c7-040eeec79652 | -9.84094 | -60.31186 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fbdf22b1-95f5-3dae-9131-4e1610bf5ad5 | -9.84017 | -60.31643 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14b4c0eb-da40-3753-a39e-e1229516776f | -9.8394 | -60.321 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57819130-a630-3235-b540-eb138e5053c3 | -9.77492 | -59.81401 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8df306b-753e-34e7-80b7-b366d23b2fab | -9.77419 | -59.81832 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b52aba09-aa6a-3f5b-98a5-fc983757a731 | -10.40492 | -61.26353 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9e57c0a-0cd3-3f56-81b6-ec6240f07b64 | -10.40147 | -61.28339 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7a0f8b2-02d1-3158-8799-f4c86ca1c79d | -10.40097 | -61.26286 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78d17e36-e6f0-3186-9011-4e2b041ded2c | -10.40056 | -61.28864 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79840d09-43c8-3b47-8ff8-dbf7183e662d | -10.40012 | -61.26775 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4039c0dc-10cb-35ba-aa8e-2a33f338cd96 | -10.39755 | -61.28251 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dc99677-13c8-374a-8b5d-0e052ad0ebb2 | -10.39662 | -61.28784 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62638281-a3f3-3aa7-9985-fad231b34dd3 | -10.39361 | -61.28178 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 367dbf82-3f07-372b-9002-87738efd416f | -10.38112 | -61.19484 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ce41522-849e-3e2b-b546-48afe3e2e776 | -10.38084 | -61.19244 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 310a877b-cc6e-3239-a5a8-b95e44f48604 | -10.37997 | -61.19743 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcd16b1f-741a-31ce-82c7-152ce85a3193 | -10.3772 | -61.19412 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cc19983-f6f9-3444-8637-7ac19d77497b | -10.37635 | -61.19913 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1deff32d-7a87-316d-a2df-e0ebd4fe9f62 | -10.2227 | -60.50126 | 2024-10-13 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9edc4b9-d7bc-36d6-a5ef-f1417a022085 | -12.1538 | -60.74856 | 2024-10-13 05:04:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f51d78f-78eb-3dfa-8ef4-6023ad48d412 | -12.15303 | -60.75306 | 2024-10-13 05:04:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 69d06434-d812-32e3-9370-121fbf1e6932 | -12.15226 | -60.75759 | 2024-10-13 05:04:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c5fb8b14-d42e-3dbd-861f-db35030dab58 | -12.14931 | -60.75235 | 2024-10-13 05:04:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6adec3b-cb3e-3f25-b5f1-c165927eedb7 | -12.14713 | -60.74261 | 2024-10-13 05:04:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef778f42-4c7d-3ca9-bf05-2bee6de85f2a | -12.14635 | -60.74714 | 2024-10-13 05:04:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29115b98-1090-3b44-bbdc-7ff17d224e61 | -11.34273 | -60.53359 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 284d454e-faa7-31d5-9dbc-035368ed2393 | -11.21221 | -60.59772 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 017137f3-f97a-3abe-ac07-2da45eb7968d | -11.2077 | -60.60159 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d323094-d5d7-3630-b7fc-02475b2b3b02 | -11.20085 | -60.61916 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eba2f85-c358-3117-a615-d6dfb20fdce4 | -11.09502 | -60.60291 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10e80580-1d1d-3c40-83ed-5c4cc07e042c | -11.0663 | -60.72615 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f7693e2-eab7-304f-bb04-8ef9e49ed8e8 | -11.0655 | -60.73082 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a0c1867-c7aa-3247-b1a7-5a1a9a6f7793 | -11.06172 | -60.73016 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7687e08d-acc6-35fa-b1ab-63bcdeddc916 | -10.95754 | -61.10519 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ee7d8fe-9109-3770-91b3-fd2490305606 | -10.95238 | -61.13477 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2df4620-59d1-3920-82ab-66cf589e597a | -10.95067 | -61.09884 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a68c1251-57db-3921-bf29-a5eb198b8069 | -10.94995 | -61.10104 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0229fecb-da98-3341-b866-9cc79bdd4b7f | -10.94968 | -61.12642 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e021640e-6c50-3c72-878d-12db2a069e94 | -10.94938 | -61.12901 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e21d5886-c8bc-3cb9-aa0a-a5debde8ddb0 | -10.94884 | -61.13139 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9534cc96-67b3-3150-8a30-3d4ce72101d7 | -10.94851 | -61.13404 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24a13479-5873-3cdb-a36e-411e2b5be8b0 | -10.94681 | -61.09808 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9c621ab-4517-3801-8de5-7d3413e7c432 | -10.94608 | -61.1003 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47e746d4-4b24-36db-9356-5723bfa5aeb1 | -10.94597 | -61.10289 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3dea09b-ab12-3761-b46e-f5c80c692293 | -10.94551 | -61.12832 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b60792e1-55c6-33dc-9607-bd03de4bfdfd | -10.94496 | -61.13068 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fabf08ac-94d6-3ed0-9155-1eea28eb5602 | -10.94463 | -61.13333 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47d5dfd6-c746-335b-b50d-0e2de3bfcb6c | -10.91879 | -61.34984 | 2024-10-13 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c17e265e-c726-3a5a-81a9-9183fbeb5de3 | -11.3546 | -60.55435 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b34f8a3e-8b44-313c-9427-112484ccf554 | -11.32412 | -60.53011 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0406a4a-8e54-304c-9555-0f2a14358a2a | -11.30674 | -60.42982 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b438f21f-9f60-35ef-8afe-4c03e32a2f29 | -11.30595 | -60.43446 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e042aefb-63bc-3714-a680-35f06aca0523 | -11.30517 | -60.43903 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bc59bd7-79f7-329b-8aed-8486938aaac6 | -11.30441 | -60.44346 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 58416486-192a-386a-ad8f-19d98e9d42b6 | -11.30302 | -60.42926 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55ad9dd0-fc5a-39e2-9343-4634da5b1e54 | -11.29928 | -60.42878 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eadd1f3c-fba1-38d4-953c-2602c28aa12a | -11.28068 | -60.44804 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2e555ace-fcf1-3911-8fcb-ac752d0c4027 | -11.27993 | -60.44578 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f10596b-b29f-3341-b846-71cce01a8532 | -11.27991 | -60.45248 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 253c591a-d5a8-33ad-b4ee-a06890080a86 | -11.2792 | -60.45021 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8a5180be-406c-32b8-aa75-4c1d1e48f51d | -11.27845 | -60.45471 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2acf3523-8ca7-3f18-9a3f-4a954ce0237c | -11.27694 | -60.44754 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 735ed25c-7e51-3fb0-9e7d-4e83ef5ab401 | -11.2768 | -60.47055 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4867f544-86f9-3d8a-a750-d45c733c9f5d | -11.27619 | -60.44535 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b7aba68-32e3-36aa-92e0-a4298a2c3fa3 | -11.27616 | -60.45205 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f9861d09-0911-3279-924c-b883aa45359a | -11.27544 | -60.44984 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| afded06f-a151-347b-9cd0-23cb924393bb | -11.27543 | -60.47289 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f6bc137-e688-3b87-8ec1-b73bf95ea7ba | -11.27406 | -60.36668 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca4d483e-075e-326f-bb52-dcb09bd741af | -11.27395 | -60.44273 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 673590f3-97e6-38d3-9552-1896dab815f7 | -11.27317 | -60.44722 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README88.md)
