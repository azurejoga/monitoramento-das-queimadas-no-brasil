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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a75cf28-fbcf-3efe-ac27-84701de85e93 | -16.83243 | -55.8978 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 3202ecc1-24a2-3c47-bc8a-7b15172040a5 | -16.83162 | -55.90041 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 62e79c3f-c5d9-3624-b119-ba35cb84f62e | -16.83119 | -55.8787 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ac40bbcc-cbbd-31af-ab0b-f147e3b75ddc | -16.83117 | -55.90705 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b6b7702d-2de0-3ca2-b86d-b3682297253f | -16.83057 | -55.88334 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d673596e-497c-3be4-8830-0c2ebda741ab | -16.83055 | -55.91167 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f3e8135e-bb61-3ce7-9b35-bd18633112e7 | -16.8305 | -55.88135 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| bf15c86d-9a36-30b3-bbae-ca263b5cac35 | -16.83031 | -55.90965 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a6daa40e-b2b4-3865-a441-be8877563ed5 | -16.82984 | -55.88598 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 16163434-fc35-38b7-aa0a-69c93bfa88a0 | -16.82919 | -55.89061 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 402ec79f-1295-34af-9561-bbb8bbee24de | -16.82806 | -55.90187 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 8f45f2fb-4e58-3b5f-ad34-347b73e346fc | -16.82745 | -55.87814 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cbb3b9e5-cb36-31e5-bb9b-55bcab8b7ca0 | -16.82682 | -55.88278 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0650b3ab-98ca-3ebf-ba18-95020b401c85 | -16.82676 | -55.88079 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 12b719a2-1d5c-3e54-b139-509886746290 | -16.82658 | -55.90908 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| b180fa33-f062-34fe-a77f-5289ca207166 | -16.8261 | -55.88543 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8a042db0-95e4-3cd0-9e0f-c619a8a9c246 | -16.82593 | -55.91369 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 630982cb-4f68-39c6-ab47-765bd2c6aae1 | -16.82366 | -55.87561 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5b97e39c-8d0d-3d13-a541-add9151769ce | -16.82284 | -55.90852 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 71933501-4537-35c7-b2b6-e51bcd73c1b9 | -16.82236 | -55.88487 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 58df2163-007f-330f-8a5d-611ed3e0f04f | -16.81992 | -55.87505 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 627173b5-e17e-387f-9d23-1cf59a4c6442 | -16.81927 | -55.87969 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5245ad6c-f2bf-3320-a04a-438a7a41a811 | -16.81846 | -55.91256 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 280318db-6309-3a67-b7b4-b5f04c299c33 | -16.81797 | -55.88894 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 9651de8a-9ecf-39c6-9abd-9011b719c228 | -16.81732 | -55.89356 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 26906954-b886-36c8-bbd6-89e8fb0b81da | -16.81683 | -55.86985 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c4afebd7-f803-3f51-9f60-215d6f8bfbc0 | -16.81618 | -55.8745 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 99454ff7-e904-37a9-bbf9-0d61f5273edc | -16.81422 | -55.88837 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8d700933-43df-3fe9-9113-731ddd4e92de | -16.81243 | -55.87394 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a65c3ad2-196d-3433-a0fc-28b4922dc4bd | -16.88224 | -55.92411 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d42306bd-2d07-3dbe-97bc-6e61ab9d6b13 | -16.8816 | -55.92872 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| aab14605-e47d-3a28-b1fa-bc2317dc3ede | -16.87914 | -55.91894 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c86952d1-d167-3083-9bdf-e0bfc3c12492 | -16.8785 | -55.92356 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| eeb65f05-83ce-391f-acde-a2a4906c2493 | -16.87412 | -55.92761 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f3a1878e-b91b-3c28-82e0-99e0bb0fd5e4 | -16.87166 | -55.91783 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 743044d5-8030-391b-bc9e-039cf7f7c7d6 | -16.86792 | -55.91727 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 6b126d5e-ecf3-316d-b5eb-6c9f0e11f1f3 | -16.86419 | -55.91671 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3540981c-c83b-3f0e-a715-23323468e23d | -16.86355 | -55.92131 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 86313894-a32c-38c8-adf0-eeb701935c74 | -16.86158 | -55.96333 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f2d5db0e-99e5-3d65-9188-6853081571bc | -16.85785 | -55.96277 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 745b69d5-6b59-3824-8e30-619130529bf6 | -16.85671 | -55.91558 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5e20502f-9a81-3032-b18d-4e897702f14c | -16.83423 | -55.96858 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ee23aa54-1ec3-3465-8aed-ed7fc7fe447c | -16.83361 | -55.97316 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e456e368-8ff4-367f-b20b-9626560473be | -16.82992 | -55.91629 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b2dab990-fd32-38ce-854d-d546ac17b2e6 | -16.82901 | -55.91885 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 59b4dec8-30d4-3399-a5e2-5f16ec734bf7 | -16.82556 | -55.92034 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| abce4633-1ff3-3cca-b76f-8b7bf5e2e700 | -16.82245 | -55.91516 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9554fc07-2c3f-3d34-a9a4-a1234ddc61f7 | -16.82243 | -55.97148 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 2d5f3f91-26a5-30cf-b682-954fd652f44d | -16.82185 | -55.96935 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 56539325-5286-3e27-be84-8f27a1165215 | -16.82089 | -55.92234 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e68e441b-3194-30c1-a958-e6e6c3d4eaec | -16.81933 | -55.96634 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e38ec272-5e16-3432-8393-e3ae142d7ae3 | -16.81871 | -55.97092 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| a3862bf8-1d10-3085-9ab5-f019cca6ca5f | -16.81813 | -55.9688 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ff0927de-1fe5-3d8c-84af-b48b71456854 | -16.81781 | -55.91717 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| a3594fbb-3971-31ee-a729-38be6e4843e1 | -16.81716 | -55.92178 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 23c3d992-42bf-3bb8-bd57-ef63187d5036 | -16.81441 | -55.96824 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0a600b2f-ca1b-348d-80f1-eeb658813b27 | -16.81343 | -55.92121 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 117d4de1-4b61-3e32-83d0-251d1969c22c | -16.80775 | -55.93446 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 0c6a1dfb-f3c5-33ac-9ff8-48b8a91b056d | -16.80259 | -55.97115 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f4278346-7e16-3b6c-a12d-caf6498e790d | -16.80094 | -55.92873 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f525d6f5-6204-3ff1-8017-82b98fbb0ce3 | -17.28144 | -56.41809 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ed46a690-65df-3244-9882-2ca678744fcf | -17.10913 | -56.69114 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6cec213e-f79a-3a74-91ff-5b666e045103 | -17.10852 | -56.69541 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fc1cc1d1-874f-3588-b40b-03e0ebad892b | -17.09468 | -56.71511 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| dce82066-241b-30cb-acae-4e3bea3574c7 | -17.08869 | -56.70547 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 366f0151-ef90-3afa-9d8f-cc2f3bb7101e | -17.07611 | -56.37313 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fb103f4b-de6f-3584-a321-69a84cb6e829 | -17.07548 | -56.37755 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 49f474fc-ccd1-3caa-9ba2-46e901f23080 | -17.06869 | -56.399 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f41f9034-eb90-3bf5-88d8-9d94db279486 | -17.0677 | -56.69788 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1de44138-feb0-314b-8b70-b9d6fa7ac872 | -17.06709 | -56.70216 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9bc4231f-f8e7-336d-9746-bfb86d2f3d20 | -17.06691 | -56.38524 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d2f811f7-97cd-3009-b2b9-58111d2da1e3 | -17.06388 | -56.38028 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 461d34c2-5737-361c-8f9b-ddb61f70c9ec | -17.06326 | -56.38469 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4837af9b-b3aa-3f52-978d-0a4f0307a14d | -17.06289 | -56.70588 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 4b36437a-ca2a-389f-b21e-727b64fb98dc | -17.05989 | -56.70105 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| cfe9fa18-295a-36dd-8b6e-479d1d556336 | -17.0563 | -56.70049 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1aa687bb-1274-3fcf-8f4c-eb01b7044c91 | -17.0557 | -56.70477 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d2182ed3-0dc5-3b60-9ab4-d2f3ab1f18cf | -17.19212 | -56.18328 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 34e76a65-87b6-3df0-b7a3-c7b6bd2b1105 | -17.19316 | -56.22947 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c436a972-559a-3e85-9171-999081ee00de | -17.19292 | -56.28441 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e7fc8922-c064-3a8a-a78e-2e441e5d8152 | -17.19253 | -56.23396 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c2a8bce2-4aa1-3703-9410-e3bd7e3dc690 | -17.19229 | -56.28888 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d9b37776-f0eb-3cda-a5f2-ebcdcbb9d45f | -17.19178 | -56.26594 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| afff2b6c-a79a-3828-a584-e6b71974a141 | -17.19114 | -56.27043 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 331489cb-9f5a-308e-ac5f-d65f6959ab86 | -17.19085 | -56.1923 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 796089da-04d3-3a96-8eb5-c4f28cbf6a0a | -17.19051 | -56.27491 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2936c08f-cf27-32da-91cb-5c23436e2615 | -17.19021 | -56.19682 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e027a434-3920-3a01-ae05-da04be99f1a2 | -17.18947 | -56.2289 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 45498698-5e23-3b35-b770-d7c9fb39d833 | -17.18905 | -56.1782 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 89b3c241-181d-383d-9da2-7155be333118 | -17.18842 | -56.18272 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6983fe46-ce4a-31a3-82a5-c14ca19ccd66 | -17.1881 | -56.26539 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 38a8d58e-2471-3634-8d82-da9d0bf97cd2 | -17.18768 | -56.21486 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 756e77a4-ecba-3102-a348-6e285c8ba4be | -17.18715 | -56.19175 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| dfd5d646-6844-374f-b277-bc0421196613 | -17.18683 | -56.27435 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d72d7a81-270b-332d-95c3-e1c68736d433 | -17.1862 | -56.27883 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c5a239b3-6528-3198-9118-352994da7ae5 | -17.18535 | -56.17764 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 7069a18b-57f9-39a1-86a9-427b1bd3d707 | -17.18472 | -56.18216 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| d4e89bd2-ffce-365b-92a6-db225ae04f4a | -17.18399 | -56.21431 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| eea2adc2-3395-3136-9c05-84840dc579cd | -17.18378 | -56.26932 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 21b6106b-bef0-32e4-be76-13832fd40273 | -17.18315 | -56.2738 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |


[Clique aqui para ver as próximas entradas](README145.md)
