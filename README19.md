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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65a4592d-b3e0-3c6d-a4f4-b94cb45a440d | -11.1443 | -45.73569 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1de88d3a-80ce-3b88-823c-f3a2efa220e4 | -11.14389 | -45.62173 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 31925385-23b8-35e1-ab18-963c2fa62011 | -11.14364 | -45.73916 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d6ad6185-285f-3933-ba5e-517c2e48edca | -11.14323 | -45.62517 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4a56abe3-736d-3f9c-881d-fa59a99a9af5 | -11.14298 | -45.74263 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4a8dd231-86c3-3547-b556-93510a18204a | -11.14258 | -45.62859 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e381f960-003f-386c-b0c0-afa2426c9186 | -11.14232 | -45.74611 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e4a245c1-1328-38e4-aa84-c40109d9ba29 | -11.14215 | -45.68872 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d710fa34-2afa-31a9-bccf-4e4c56f360b4 | -11.14192 | -45.63201 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f82f87f-e380-3d34-a5ff-7fdcf86aa1bb | -11.14149 | -45.69216 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 19f4e100-3959-38ae-b533-857666e5c50b | -11.14127 | -45.63543 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67086a0a-a160-3c42-9284-9143cf7161bb | -11.14083 | -45.6956 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b5a02666-13d2-31c5-97d7-b1bba08c0c70 | -11.14026 | -45.72775 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 498d6173-d22f-3fc7-9172-25b4ec63f42b | -11.13959 | -45.73122 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a967a2cb-cde7-3b0d-babb-6d77b9d00ed1 | -11.13893 | -45.7347 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 5e8de4a2-b0a7-3b42-b05c-ff6d82e0ae14 | -11.13789 | -45.62421 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ae9e0089-0058-3d81-b5ad-8c522ad121e0 | -11.1376 | -45.74166 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| eb6a9805-940f-3435-aaad-a10e30b1235c | -11.13723 | -45.62764 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 96bf15d9-03e2-3536-a41c-b2b3ebd54c39 | -11.13694 | -45.74513 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 4bb0c10c-b9de-3c68-bc1f-4168dd03ea93 | -11.13628 | -45.74861 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 118bc08a-93a0-363e-aa8a-8755b5e9f764 | -11.13562 | -45.75207 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 37be3cef-ceb1-36b5-be3d-ec1d194d2ac3 | -11.13289 | -45.7372 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 4e8e7ddc-e6a7-3de7-8bd3-e7b4b2c5c219 | -11.13222 | -45.74068 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| aedc1d94-a878-3eba-ad31-bff2c02a323c | -11.09618 | -45.65157 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19d2a2b0-6f23-3cb8-85dd-f66cfe8530dc | -11.09553 | -45.65504 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87de9958-e38e-3911-92f1-981cb105217f | -11.09393 | -45.65133 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c7c32f5-c301-3078-8521-f5ee3f5ca4d6 | -11.09325 | -45.6548 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccdd6ad4-eec2-31c9-ba50-06e345a8b976 | -11.05866 | -45.79245 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77091c6f-2441-3b38-baca-fbed0c63da26 | -11.05762 | -45.85765 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f882d90-9375-3ce1-929d-ec0e72971a26 | -11.05388 | -45.85668 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85c75aa1-05eb-304f-a52b-c1283d270299 | -11.04616 | -45.85888 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84a46d03-5781-3d95-9d3d-9aaa51b58111 | -11.04549 | -45.86243 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 02645037-18b4-3d08-9652-304be4b21e2c | -11.04482 | -45.86602 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ab6a1329-5d44-373a-8d1c-0dbfb6da92f8 | -10.91857 | -45.50088 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79c1cb61-a7a3-3cc1-8968-0e647d692d9c | -10.91793 | -45.50436 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb098c2e-9b3a-3e7f-8e57-2b5c4bf92bc4 | -10.91744 | -45.49924 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffe913f1-4b01-35ce-b67e-8ef6ba8e34a6 | -10.91676 | -45.50277 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5837cf62-8400-344c-bd8e-de5580d3fba8 | -10.88561 | -46.04597 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c95e0fb7-87c9-3e2e-8f53-57238816253e | -10.88489 | -46.04976 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53df70b8-7ab1-3eab-bcba-759acc328a14 | -10.88417 | -46.05356 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12347bd7-c879-3458-bd6f-db21ea2be7c9 | -10.88291 | -46.03022 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b0e390f-c9f4-3d51-80d2-b4c194364670 | -10.88217 | -46.0341 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f6eed89-ab2a-3e82-9f40-a4f243dd1aa6 | -10.88144 | -46.03794 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0dadc698-08ea-3fd9-bd9f-e8f637ecb8b4 | -10.88072 | -46.04169 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22db7967-7a98-36b9-84cf-76127c336aab | -10.88001 | -46.04544 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f741053d-6068-35d9-96b8-dc62d8fa06aa | -10.87337 | -46.02052 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84a1f459-9f4d-3d21-96d9-42d2b511e2db | -10.86945 | -45.98153 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e487279-1533-3825-93ec-dddf11845f4c | -10.86466 | -45.97687 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e5680ca-1281-349a-9d73-18076e70f8f0 | -10.85988 | -45.97221 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d1e4108-32c5-3392-b150-25d02294d41a | -10.8551 | -45.96754 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f40c9c20-09a8-3432-a000-5fd43cfcb153 | -10.85032 | -45.96291 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77b16f12-ac23-3184-a147-6d1b45cdeb50 | -10.84482 | -45.96196 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1aeaaa8-5b57-3afb-b44f-4faed0646cdf | -10.84002 | -45.95746 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ee29dcb-df8c-3602-a5fe-9ff5e93c3f36 | -10.83354 | -45.95843 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9854d70-2c6b-3e47-8f35-aee2a190a0b5 | -10.67523 | -46.16569 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53ab6663-e013-3968-8556-8f87e7dd885e | -10.67462 | -46.16157 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 745a0a8f-f89d-3ca5-8f47-65fa47fee60a | -10.67449 | -46.13898 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2de5b353-0db8-3219-b441-af1db1a10d3b | -10.67389 | -46.1653 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 89746671-098e-3333-8cd5-2f904cba0362 | -10.67242 | -46.14995 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a77bb109-304e-3adb-8b6e-2072758384bc | -10.67174 | -46.15359 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cec15ae-92d3-3696-b65d-b815ab9b6e0e | -10.67169 | -46.12327 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96d8454a-7032-3875-ab2d-503524939c43 | -10.67119 | -46.14961 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16533793-0509-3e65-964e-ea985ba71b32 | -10.67105 | -46.15726 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b65a52c6-b288-34f5-b06c-31c8d6811fc5 | -10.671 | -46.12694 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d4d924f-65aa-3403-a1e2-6478f792d0fc | -10.67048 | -46.15326 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 394bc7e3-83d9-3492-81b4-648c5dc9f548 | -10.67036 | -46.16093 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 816df535-821a-3415-9b07-036a1b918a7e | -10.67031 | -46.1306 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5802d4a4-ac54-316d-81b1-3752fde9459b | -10.66976 | -46.15692 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0381e53-e45d-3a35-938f-2a14a5d4bb94 | -10.66965 | -46.16466 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2039c92-1331-330f-baf1-be991c78e155 | -10.66962 | -46.13426 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79d4b54d-a485-3c07-9f64-bb03dcea4260 | -10.66904 | -46.16059 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6802bc85-5065-3209-aaa4-05e2fd02610f | -10.66547 | -46.15627 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f92821d-7178-3057-9258-662a86244f65 | -10.2607 | -43.55896 | 2024-09-30 03:45:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e55e221-2eeb-3821-a022-ad3ee986b3f8 | -8.81772 | -46.77979 | 2024-09-30 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 636416f1-b694-3d46-a0f9-f066c3bae15e | -8.81688 | -46.78408 | 2024-09-30 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad3f1e01-e616-30f8-b8e3-53dbee921737 | -8.81605 | -46.78838 | 2024-09-30 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 713d14a0-e854-3eea-a4aa-d2c1d60aaabb | -8.43073 | -46.36445 | 2024-09-30 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b80415d-2906-3a86-886e-230715d3aa09 | -8.42994 | -46.36868 | 2024-09-30 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae6b8f89-a85a-3283-9fcb-3f2e9abb066e | -8.42799 | -46.34671 | 2024-09-30 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 912e3f35-baee-39b5-814d-ba1a438dadee | -8.42227 | -46.34495 | 2024-09-30 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15ac2e4c-24a7-39a1-b326-69d6d90b7c72 | -8.41641 | -46.34389 | 2024-09-30 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f77331e6-dba6-3001-888d-fea33ea3fb98 | -7.351 | -44.77448 | 2024-09-30 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72411672-ecd7-36b2-8e41-9b6b68ac29d3 | -7.34563 | -44.77341 | 2024-09-30 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffc4822e-a00a-3002-8338-54ac82be8ae5 | -7.24874 | -44.93905 | 2024-09-30 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3772ad9-0058-3bc6-95bb-a8c341147395 | -7.24834 | -45.00319 | 2024-09-30 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90ff1bae-9478-3aae-ae25-3cfa08778e83 | -7.24806 | -44.94278 | 2024-09-30 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f543b9db-608f-3cc3-83f1-2fc0b3bc6689 | -7.24769 | -45.0068 | 2024-09-30 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8806635-ba60-3038-912d-1e4f3e4aeff9 | -7.24703 | -45.01042 | 2024-09-30 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90312b29-7ac4-3e4c-9a03-c77dee8771db | -7.24264 | -44.94164 | 2024-09-30 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d747f6e-f063-3521-9c4b-2b08dcf5c824 | -7.24093 | -45.01286 | 2024-09-30 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9267589b-7922-3a5d-b577-bfbf00c9a04c | -7.24027 | -45.01649 | 2024-09-30 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8dd1cee-71fa-34f1-94fe-506cdb6529d4 | -7.06159 | -46.22405 | 2024-09-30 03:45:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1487947c-fded-31c3-8163-85a5e7e42762 | -7.05561 | -46.22317 | 2024-09-30 03:45:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea783317-b04b-3eda-bbd0-517ba739c7a6 | -6.97701 | -47.63418 | 2024-09-30 03:45:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1ab7456-0baf-36e3-9ee5-727e22e5c184 | -6.97599 | -47.6398 | 2024-09-30 03:45:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5fc453b4-045c-3507-8473-93f0f16f2b01 | -13.58273 | -51.09543 | 2024-09-30 03:45:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1d133094-6271-3799-aa8b-0710dbebc92c | -13.57567 | -51.09386 | 2024-09-30 03:45:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c48974d4-ebf9-343b-b16c-1f564d2d6815 | -13.20856 | -48.55824 | 2024-09-30 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 912102c7-1dbb-31ec-af83-0a9df726e145 | -13.20714 | -48.56517 | 2024-09-30 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 09c33021-8ce6-3fe7-b111-97499f91b582 | -13.18512 | -48.54721 | 2024-09-30 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README20.md)
