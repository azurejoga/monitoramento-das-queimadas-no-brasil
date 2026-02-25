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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 763f60f8-b319-3676-8f1d-153afc18d33c | -9.9696 | -36.2531 | 2026-02-25 00:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 135.0 |
| 0c077b06-f101-3ace-9362-0f6e0ea3ec1b | 1.5229 | -59.9495 | 2026-02-25 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 55240dc8-3d1d-3c16-b39d-926e9407e523 | 1.4864 | -59.9308 | 2026-02-25 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.2 |
| c50f0cda-94a9-3b2a-a9e2-cf525448aed5 | 1.5046 | -59.9306 | 2026-02-25 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 200.5 |
| deedd291-88e5-3393-8721-77fdba8bf8ca | 1.5229 | -59.9305 | 2026-02-25 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.7 |
| ac1c903d-60cb-3525-973e-66aec8606617 | 1.4864 | -59.9498 | 2026-02-25 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 27395108-7b8e-34fc-b734-0d05c86cdb86 | 2.2333 | -60.7207 | 2026-02-25 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 65695a3a-8cbe-34b8-bcfb-8d873bcd33c5 | 2.2333 | -60.7018 | 2026-02-25 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 175.0 |
| e9dadaa9-c30f-3f76-a181-c61d54477e95 | 1.5046 | -59.9497 | 2026-02-25 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 193.2 |
| 24c34c35-8bd9-3172-9fdc-24989a8d3ed7 | 2.2333 | -60.6828 | 2026-02-25 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 7e86eac8-aa7e-343e-8d46-dc318e35ca73 | 1.9412 | -60.8565 | 2026-02-25 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 58080738-128f-3dcc-8bcd-c32a2dd66b71 | -9.9691 | -36.2802 | 2026-02-25 00:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 71.8 |
| b92e6cf0-519e-36c0-a273-2c926967d788 | 2.2333 | -60.7207 | 2026-02-25 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 792968f5-8437-34e7-8742-80b38147abd2 | 1.4864 | -59.9498 | 2026-02-25 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 07540d78-d940-30f1-a897-fb84008274d3 | 1.5229 | -59.9305 | 2026-02-25 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.8 |
| b1465bd3-03e7-3a45-8ad2-6c7862e3ca76 | 2.2333 | -60.6828 | 2026-02-25 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.9 |
| a74e4775-a8a2-3373-8086-211df2177295 | 2.2333 | -60.7018 | 2026-02-25 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 198.2 |
| dff071ff-7cae-3c8d-b9a1-e5e5fbb31e40 | 2.2515 | -60.7015 | 2026-02-25 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.8 |
| a32583bd-dd07-39c6-b60d-00ba1a2006c0 | 1.5229 | -59.9495 | 2026-02-25 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.8 |
| d717c416-be15-3c7e-8044-2d8379b4bc39 | 1.5046 | -59.9497 | 2026-02-25 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 182.1 |
| 5fa24081-8707-34eb-825a-ca353ce90917 | 1.5046 | -59.9306 | 2026-02-25 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 184.5 |
| a9ac4172-01e5-3cdd-82d1-1214b3b67a03 | 1.4864 | -59.9308 | 2026-02-25 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.3 |
| bc6d2ab0-9058-3e8b-8740-521d248828d5 | 1.5229 | -59.9495 | 2026-02-25 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 3895413a-1521-35a6-a09d-3351ab529cb2 | 2.2333 | -60.7207 | 2026-02-25 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| b6326d36-8984-361c-b7bc-7a23227d84d4 | 2.2333 | -60.7018 | 2026-02-25 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 197.8 |
| 8bca938e-7024-3f44-abef-398f0505c5d5 | 2.2333 | -60.6828 | 2026-02-25 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 33be6fff-df44-3e36-807e-1292bdc963a6 | 1.5229 | -59.9305 | 2026-02-25 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| e99700ff-f5bd-39f3-92a8-476a23eb0618 | 1.4864 | -59.9308 | 2026-02-25 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 00343536-0f7c-3356-848e-90212ec7574b | 1.9412 | -60.8565 | 2026-02-25 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 01bedb66-861f-3ac4-a83f-abd6216870b0 | 1.5046 | -59.9306 | 2026-02-25 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 167.0 |
| ca334065-9a81-39eb-a79e-29976561a283 | 1.5046 | -59.9497 | 2026-02-25 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 198.7 |
| 9eb07ac1-fab7-33dd-8d8e-f77e65a92db1 | 1.4864 | -59.9498 | 2026-02-25 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 4b2078e6-44af-3e04-9693-960b86e2c7c1 | 1.5046 | -59.9306 | 2026-02-25 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 211.5 |
| 0f6a658a-713a-3fc3-9731-e8d8fc5aa039 | 1.4864 | -59.9498 | 2026-02-25 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.6 |
| bf0867e2-6a0e-3a02-bd28-ae2a102693c9 | 2.2515 | -60.7015 | 2026-02-25 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 0fa1f889-6894-3234-a0ae-a37d6b75a30a | 1.5229 | -59.9305 | 2026-02-25 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 68627563-6266-3512-8f96-ac7c433bce15 | 2.2333 | -60.7018 | 2026-02-25 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 133.3 |
| d80c0041-97ba-3f4e-845b-cc0f8b3ce29c | 2.215 | -60.702 | 2026-02-25 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.5 |
| dea2494a-8a86-3922-a920-5e6ac97e9e60 | 2.2333 | -60.6828 | 2026-02-25 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b56d3918-a400-3197-bde6-88f4c2523253 | 1.5229 | -59.9495 | 2026-02-25 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 7761a357-6807-3450-8657-affd732ee3f8 | 1.5046 | -59.9497 | 2026-02-25 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 186.3 |
| 90804c3e-8039-3b4d-9cb8-8cc0585cd0c7 | 1.4864 | -59.9308 | 2026-02-25 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.4 |
| fb272a0c-9b14-3e2a-9dee-21f0e6048b9f | 1.4864 | -59.9498 | 2026-02-25 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 0511e27d-a67f-3c64-96ea-f321f00cbfb9 | 2.215 | -60.702 | 2026-02-25 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.6 |
| ea3a591b-3415-3b2a-906c-c3c24347f077 | 1.5229 | -59.9495 | 2026-02-25 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 6906dbd9-a295-348d-add1-0766023f8c82 | 1.5046 | -59.9497 | 2026-02-25 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 169.1 |
| fbfd0920-e09c-30ae-a503-83c8509f0d80 | 2.2333 | -60.7018 | 2026-02-25 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 145.7 |
| 095edc01-283a-336e-8a8e-ed377a1f8638 | 1.5229 | -59.9305 | 2026-02-25 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| fc7fbf53-069f-3c6c-9f94-de2d00e96c2d | 1.5046 | -59.9306 | 2026-02-25 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 4a0eb675-2e4c-3b50-9a89-cafc49196e99 | 1.4864 | -59.9308 | 2026-02-25 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6301ad86-694f-3307-9a92-1e1c259a0508 | 2.23776 | -60.70515 | 2026-02-25 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 109.7 |
| c413bdf7-95c4-376c-b233-b9d8a79be461 | 3.44869 | -59.89124 | 2026-02-25 00:49:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1633c482-deed-32c6-8014-ce9a3b41a094 | 1.50613 | -59.94553 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.3 |
| a356cdfc-c8bd-3e77-b7fa-5b7259cfc2eb | 1.94723 | -60.366 | 2026-02-25 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fd83410b-5a86-316f-bd19-155924f2cfcf | 1.50466 | -59.95601 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.2 |
| dda2d55b-6ab2-3bf0-a03c-916facd7c546 | 1.88127 | -60.91526 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 32b6c72e-238e-3dab-b111-c5be9f414853 | 2.71956 | -60.25005 | 2026-02-25 00:49:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 04b53e46-4e85-3547-8447-da428f4f0fd8 | 3.93322 | -60.06216 | 2026-02-25 00:49:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f1eeda1f-ef0a-3718-98ba-0b11ca3c9e2d | 1.30787 | -60.40326 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| fa0d796d-f165-306e-bed7-de497b071db4 | 3.69964 | -61.92068 | 2026-02-25 00:49:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ae5f9a0c-5d2d-30d8-9c60-d813881953ae | 1.94003 | -60.85748 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 53f2c4bb-dfa2-3fa5-98bf-4883a27de5a3 | 1.00558 | -60.44596 | 2026-02-25 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7574701b-602e-3777-a5ae-6371314a0e3f | 1.49655 | -59.94414 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 850b76d8-69bb-3a20-a3c4-235e688fd45a | 1.50761 | -59.93499 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d9b68394-ec85-33b3-8c03-53552d58cf6c | 1.52315 | -60.03412 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ccdce22f-3151-3798-b7e2-629bebd8bd49 | 4.22496 | -60.19939 | 2026-02-25 00:49:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| eb7612ba-7144-3dbb-97e9-e32e47f14f29 | 1.51571 | -59.94691 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.3 |
| a7a183f1-4cec-3579-aba1-e16b36d0209a | 4.23581 | -60.1906 | 2026-02-25 00:49:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 23.5 |
| d10114b0-44f9-3f7d-aa72-8bad771205ea | 1.49506 | -59.95464 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| eca7c73e-65e5-3a68-9589-327b4aaefc07 | 1.00717 | -60.43452 | 2026-02-25 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c874d9ee-81b0-3e65-9e2b-9a4461ceb35d | 3.71029 | -61.92217 | 2026-02-25 00:49:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| fdc183dd-8264-3283-bef6-e8cda715e853 | 3.93183 | -60.07216 | 2026-02-25 00:49:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| df953810-aa87-3920-b364-783ff4c05ec8 | 1.93744 | -60.36459 | 2026-02-25 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| be6b2610-02a6-3775-872e-d41b3401433d | 1.17564 | -60.40129 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 391f6c98-1575-3244-b9a0-365ca73318c8 | 2.23939 | -60.69369 | 2026-02-25 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 4e406fd2-3bec-3b26-9303-83907b0e8d45 | 1.36511 | -60.29226 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0506cb21-daca-38ac-b465-496fc93cce27 | 2.2278 | -60.70367 | 2026-02-25 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 627e839f-7b70-3d01-9ba7-9cfc6643f8eb | 2.22943 | -60.69225 | 2026-02-25 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.1 |
| be9ec134-707c-3d69-ba78-10592cc71026 | 2.71287 | -60.2276 | 2026-02-25 00:49:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 01076c37-60ce-33f2-806d-ae8e0df96102 | 1.51718 | -59.93644 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 1f69d800-0d10-3160-9de6-a37f97a99dfc | 1.49804 | -59.9336 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| a910345c-bf0d-37ba-94a3-21b1136a7505 | 1.94169 | -60.84574 | 2026-02-25 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.0 |
| e3074b7b-6a28-3b71-906a-acbe5190fc12 | 4.23439 | -60.20056 | 2026-02-25 00:49:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ad8b6759-a5a2-3940-a963-4ead2359866c | 1.5046 | -59.9497 | 2026-02-25 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 4a8cf390-d4df-314f-b8fc-9d76306b59d6 | 1.5046 | -59.9306 | 2026-02-25 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 2ace30f2-a50c-3f2f-bfd0-524ad23745a5 | 2.2333 | -60.7018 | 2026-02-25 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 087187e0-dbfa-3292-a857-9f3053a8f72f | 2.2333 | -60.7018 | 2026-02-25 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 91.5 |
| d7f5db3f-7115-37a7-af09-b4ee69d6659b | 1.5229 | -59.9305 | 2026-02-25 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.2 |
| e589a627-9ee0-3796-b2ad-c5d3b969fcd7 | 1.5229 | -59.9495 | 2026-02-25 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.2 |
| eb3a2246-32cb-37f0-80a1-b98ce90aa2da | 1.4864 | -59.9308 | 2026-02-25 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 1a7abc8d-1f4a-33b0-a041-3c1a7a0cc407 | 1.5046 | -59.9497 | 2026-02-25 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 804ecf60-f0aa-36dd-82ec-3d466c097806 | 1.5046 | -59.9306 | 2026-02-25 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 92a45ba5-0ad6-381f-9e5c-34768c2949c1 | 2.2333 | -60.7018 | 2026-02-25 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 85.9 |
| ca56b250-7ad4-39cd-838d-1c212b4e3f93 | 1.4864 | -59.9498 | 2026-02-25 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 78a218f1-22e2-33ba-9d3d-3e66809893a4 | 1.5229 | -59.9305 | 2026-02-25 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |
| a9b5df13-54d6-3081-bfcc-bf9780acfe12 | 1.4864 | -59.9308 | 2026-02-25 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.0 |
| e4cc6a13-df14-3923-b4f0-f2716473b863 | 1.5046 | -59.9306 | 2026-02-25 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 7f3975da-7df1-3a0e-930e-818bc53e85f3 | 1.5229 | -59.9495 | 2026-02-25 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a3f7be6a-3df4-3e87-9c09-33486691adaf | 1.5046 | -59.9497 | 2026-02-25 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 124.8 |
| ace4464b-62c0-39f6-b640-215b9210fe37 | 1.5229 | -59.9495 | 2026-02-25 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |


[Clique aqui para ver as próximas entradas](README2.md)
