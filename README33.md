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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d8fb22e-33a2-35ac-a207-318e476ff830 | -18.5993 | -57.2629 | 2024-10-09 01:16:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 4a5cc402-8c78-31e6-8e6b-eca376467c25 | -18.5996 | -57.2422 | 2024-10-09 01:16:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.5 |
| f4797ed6-b5cb-342c-aca7-1b4528a58d6e | -18.6597 | -57.2137 | 2024-10-09 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 65a770c1-5453-37c6-b358-3b9d75005bb6 | -20.0122 | -42.4541 | 2024-10-09 01:16:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.7 |
| de38bd80-c698-3e16-9ea4-24f30a7c69fe | -20.013 | -42.4287 | 2024-10-09 01:16:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 144.0 |
| 887ec6dc-9efb-357b-905b-b0f171cb77ed | -20.1087 | -48.8261 | 2024-10-09 01:16:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 98dc11c4-e993-375e-b3d8-d70208b71f39 | -20.2915 | -43.9444 | 2024-10-09 01:16:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.8 |
| d222da5d-d78d-3949-8819-459b3c70d09b | -20.3755 | -48.7217 | 2024-10-09 01:16:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 3d0289c8-75a6-36c6-8abc-c4e441405f64 | -20.3761 | -48.6986 | 2024-10-09 01:16:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 106.4 |
| d42024ed-813a-34e1-b9a8-0e88c2fb16a4 | -20.3346 | -48.7307 | 2024-10-09 01:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 2ae14c82-7b26-3da4-a2a1-5f5cc774b28a | -20.3352 | -48.7076 | 2024-10-09 01:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 90ade1c6-6cb3-3197-9ddf-3865fb010be7 | -20.3551 | -48.7262 | 2024-10-09 01:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 289.7 |
| 95f64750-bf49-32d3-b2a4-3bd472d30d08 | -20.3557 | -48.7031 | 2024-10-09 01:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 241.8 |
| 171d9cda-4235-30a5-8494-30df96b6ba8c | -3.56919 | -54.34415 | 2024-10-09 01:17:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7871758f-3742-3cdb-8898-bc3e0cc43cb9 | -3.56794 | -54.33518 | 2024-10-09 01:17:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| e5430237-7eb0-35e7-97de-9ffaa172e3d6 | -3.56153 | -54.35432 | 2024-10-09 01:17:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 32464625-0653-3a64-bdb9-9279a9118e2b | -3.56028 | -54.34537 | 2024-10-09 01:17:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 8301bdc5-01bd-396d-8266-f2b1011992ca | -3.55903 | -54.33638 | 2024-10-09 01:17:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| aa9e940a-dd8d-3141-9302-eac4f2ee035b | -3.33545 | -53.393 | 2024-10-09 01:17:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 16ae0bb7-d1ec-3691-b367-8097c347bfe8 | -3.27831 | -54.17649 | 2024-10-09 01:17:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 285cfa29-7bb1-32ec-8832-cd384aba1eb6 | -3.26304 | -54.19666 | 2024-10-09 01:17:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4474315e-f7a3-3312-8ff5-2a8a115f101f | -3.26181 | -54.18781 | 2024-10-09 01:17:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| a56d2bc5-7bb4-316b-9d9b-a458ef7e181e | -3.26058 | -54.17896 | 2024-10-09 01:17:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 63c163ed-7a1c-3023-af5b-129768590ed8 | -3.15825 | -54.56351 | 2024-10-09 01:17:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ef2ccb3c-8ecb-338d-bc1e-e2ab33ae9638 | -3.12607 | -53.7453 | 2024-10-09 01:17:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f38bde70-7e2b-3436-89d3-45852244792a | -3.12484 | -53.73652 | 2024-10-09 01:17:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 3fd8000e-c157-3a1c-9139-8de3b94d5ade | -3.08923 | -54.53369 | 2024-10-09 01:17:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| df2a1216-a404-3dce-a4aa-73a5800c80d9 | -3.08031 | -54.53495 | 2024-10-09 01:17:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cbfc0f6d-482e-3778-9201-bee578c5d67c | -3.06684 | -54.77319 | 2024-10-09 01:17:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 575b29da-3582-334c-842c-0286ec15da7d | -3.04777 | -53.04107 | 2024-10-09 01:17:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 87e8ba03-b749-3cae-9aae-2bbb2dd890e9 | -3.03891 | -53.04234 | 2024-10-09 01:17:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 41206780-ef3a-33cd-8579-303d75559277 | -3.0143 | -59.11608 | 2024-10-09 01:17:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| a84b2431-1300-3077-b5fa-f3e7f7ed7835 | -3.012 | -59.09938 | 2024-10-09 01:17:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 4ecac506-480a-344e-b90d-be3f1798a4d6 | -2.97742 | -53.72782 | 2024-10-09 01:17:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 6e0503c1-aab5-3b3f-b403-27ad61d0d681 | -2.9762 | -53.71904 | 2024-10-09 01:17:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| d2043ba1-465d-3631-b482-bbef78e519d1 | -2.97498 | -53.71026 | 2024-10-09 01:17:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b3f7c68a-7d5c-3e63-a02c-25bb70715e07 | -2.94729 | -53.70522 | 2024-10-09 01:17:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7bf3a04e-5adf-3e4f-a713-1184fc2ecade | -2.939 | -54.17905 | 2024-10-09 01:17:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4cb728ec-ddad-3584-bf63-3a07c96ec7fb | -2.89998 | -50.71349 | 2024-10-09 01:17:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 96c2e3e0-5fec-38c1-a704-c074ffa090de | -2.89592 | -50.40362 | 2024-10-09 01:17:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f2c7e075-4215-3ba7-90e6-c8be25fc08de | -2.87939 | -53.95988 | 2024-10-09 01:17:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| e2154178-813e-3d45-851c-6877f643f15d | -2.87056 | -53.96113 | 2024-10-09 01:17:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 96f2dd3a-f7f6-3b24-8ca7-791f8238bc78 | -2.86234 | -51.02201 | 2024-10-09 01:17:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f34ecace-be44-35d7-99e9-fe938f1aa4dd | -2.84671 | -53.32207 | 2024-10-09 01:17:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 8bd721ff-129e-3ac5-92da-35e508ed73ae | -2.84548 | -53.31326 | 2024-10-09 01:17:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7cbd69ac-affb-322f-bf41-d7845c4980f9 | -2.84354 | -52.96436 | 2024-10-09 01:17:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a5373fdf-567c-362c-ad43-ce738afd08c7 | -2.81625 | -54.3622 | 2024-10-09 01:17:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 7c96e252-6cbd-3007-88b4-151728452042 | -2.81234 | -49.0191 | 2024-10-09 01:17:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 79864ca1-c0ed-399b-a0dc-e48f53d9fc5f | -2.81162 | -54.59057 | 2024-10-09 01:17:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 86f749e5-abe5-3e2b-9482-3f92f30534c0 | -2.81028 | -49.00458 | 2024-10-09 01:17:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 06a2902f-928b-3b69-81c3-0fd87ba396b8 | -2.79064 | -49.59144 | 2024-10-09 01:17:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f90e84b8-b9a0-30b6-81a2-e8d823df5942 | -2.74203 | -53.95829 | 2024-10-09 01:17:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 340d3e34-80c7-3348-a801-7092805cacd7 | -2.72437 | -48.7286 | 2024-10-09 01:17:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 3fd03109-a84c-3c08-aa05-016678b5ed10 | -2.60455 | -49.80267 | 2024-10-09 01:17:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| cf311baf-7b52-301f-9d86-d8a2832d7349 | -2.6027 | -49.78987 | 2024-10-09 01:17:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 6ac5e7e0-4577-393f-909f-491368677fe6 | -2.54461 | -47.23887 | 2024-10-09 01:17:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 4b76533d-0042-349d-ba17-eab1279121af | -2.54171 | -47.21882 | 2024-10-09 01:17:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| a1c997d7-8030-3fb1-a80d-b8f0a1081b50 | -2.53404 | -47.62422 | 2024-10-09 01:17:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 1476e58d-f073-3366-a1ef-00da473bb01b | -2.47985 | -48.06227 | 2024-10-09 01:17:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 71920c0d-1dfa-303c-a2bf-4976a42e02cf | -2.47447 | -50.24963 | 2024-10-09 01:17:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 8f2bb026-aa5a-38b1-9f79-a370893fce14 | -2.38792 | -47.68971 | 2024-10-09 01:17:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 28f7f709-fbd5-31de-b801-a3c1ab1b581b | -2.37542 | -47.69158 | 2024-10-09 01:17:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 25ef44a4-1f29-361f-aefc-8c68739aee59 | -2.36093 | -48.99667 | 2024-10-09 01:17:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 10f99ab1-28bb-3706-92d4-7891b666ac5e | -2.34969 | -48.99834 | 2024-10-09 01:17:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| cd4d1250-4e12-328b-b001-abe8c913ae4c | -2.34759 | -48.98348 | 2024-10-09 01:17:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9f215f03-3bd3-3caf-b70f-afbc596b914e | -2.23031 | -53.65837 | 2024-10-09 01:17:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 4cadb77e-ce21-357b-8e19-1d016c04d770 | -2.22908 | -53.64959 | 2024-10-09 01:17:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9e0d7902-aabc-3488-b66f-946300504d9d | -2.14595 | -50.88801 | 2024-10-09 01:17:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| abce469d-d720-39e9-9edb-b5258fece306 | -2.0761 | -52.03687 | 2024-10-09 01:17:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 799dfb23-33ee-3aa4-bcb0-20845201e72b | -2.07473 | -52.02725 | 2024-10-09 01:17:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 3c082b9e-9f7b-35a5-8345-5db15893a2a6 | -1.95625 | -50.84852 | 2024-10-09 01:17:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| d111f98f-f6bc-3806-b18f-89032f81cca0 | -1.64678 | -52.58543 | 2024-10-09 01:17:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d7d4dfe4-9deb-3850-bc71-151d51e0e761 | -1.37542 | -47.49049 | 2024-10-09 01:17:00 | TERRA_M-M | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 975d1489-a51d-3ab9-a0be-f7d0f120a096 | -1.26627 | -54.21003 | 2024-10-09 01:17:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4f7b1493-241c-3010-9574-d4ea011964f5 | -1.20312 | -54.22529 | 2024-10-09 01:17:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 73a8a0ad-0622-38de-a6de-a3b7b4dcfb90 | -1.13052 | -54.10731 | 2024-10-09 01:17:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| dd7602a5-b1ee-329a-b8af-0559c316f949 | -1.12115 | -53.63738 | 2024-10-09 01:17:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b4e76b96-978e-3913-b92f-7b3c54d00a53 | -1.11869 | -53.61972 | 2024-10-09 01:17:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 594f2446-2152-3bdd-ba15-ba271ff67881 | -1.11745 | -53.6109 | 2024-10-09 01:17:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 706aeae9-7208-355f-aa1d-53b5a1d866b1 | -1.11109 | -53.62984 | 2024-10-09 01:17:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 71660f48-0d6f-37c2-9c82-8d835a9c9335 | -1.10986 | -53.62102 | 2024-10-09 01:17:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 9651d2a0-44a3-31e5-9640-1a03a25f93e6 | -1.10862 | -53.61219 | 2024-10-09 01:17:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| feaf4ddc-826a-3009-8796-9409d31483cb | -1.02505 | -53.73778 | 2024-10-09 01:17:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e3960dbb-6d0a-3633-b6fd-94982b293a79 | -1.02382 | -53.72897 | 2024-10-09 01:17:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 64eedd83-3809-3a05-a89f-7f1d3c1d9b21 | -4.28847 | -60.01797 | 2024-10-09 01:17:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 5f62c903-6f44-34e1-8378-71a52dbd308a | -20.7477 | -48.5229 | 2024-10-09 01:17:01 | GOES-16 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 192.0 |
| fcbb9690-0b33-3611-b426-adb0f9589095 | -20.7484 | -48.4996 | 2024-10-09 01:17:01 | GOES-16 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 9432448c-3963-3298-98f9-7ac510336ca2 | -20.7839 | -47.2559 | 2024-10-09 01:17:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 245.4 |
| 7cde0e99-30be-3df2-830a-a7eeac3b28c5 | -20.7846 | -47.2323 | 2024-10-09 01:17:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 23dc1c16-a0d2-3145-bdf4-17cc0e71f8ba | -20.7683 | -48.5182 | 2024-10-09 01:17:01 | GOES-16 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f00f2a4a-eec9-38ad-ba6d-e023e0ff0ae0 | -21.1126 | -47.2229 | 2024-10-09 01:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 6ad16213-7472-31e9-a8d0-5de6df039ad9 | -21.572 | -46.9898 | 2024-10-09 01:17:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 111.5 |
| bd660d51-18c5-3131-b3fe-649a18a3387f | -21.5727 | -46.9659 | 2024-10-09 01:17:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 7ea3bd17-33b7-376a-b4a4-1748a4900af8 | -21.5864 | -47.8827 | 2024-10-09 01:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b451270d-9055-3e54-a948-985f8c726fa7 | -21.8373 | -49.1726 | 2024-10-09 01:17:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.2 |
| 82166b3f-c5c1-3dbb-9255-f6e2dc4916be | -21.838 | -49.1493 | 2024-10-09 01:17:06 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.3 |
| 879be9d0-b6fa-35d6-810d-d4d6f973db4d | -22.8137 | -48.4225 | 2024-10-09 01:17:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 4943731c-f4de-31b1-b6df-a74c9c84313c | -23.8419 | -51.1652 | 2024-10-09 01:17:17 | GOES-16 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 89.5 |
| 0c951be3-aa3b-3261-b840-416ad8daf69a | -23.828501 | -51.145401 | 2024-10-09 01:22:41 | METOP-B | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7aae3422-960d-35fe-9efd-e54256633146 | -23.8318 | -51.158199 | 2024-10-09 01:22:41 | METOP-B | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README34.md)
