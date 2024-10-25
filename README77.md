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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6debfb41-eb4f-397f-9ff0-89810e4fc703 | -16.92713 | -57.5281 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 8767d9eb-9642-3e0d-a5a7-f3e01bc46edd | -16.92641 | -57.53204 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a246de55-0443-3a3e-9b23-a8df056e6dc1 | -16.91486 | -57.50114 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f58f95be-8581-3a7c-bc39-8c1e6f07a389 | -16.91111 | -57.68596 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 59617da6-0a62-3ce7-838a-c30957141107 | -16.91071 | -57.5003 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| e54e4aab-094b-3b45-be4e-d60fc254c878 | -16.90998 | -57.50422 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| ab26d761-34f3-396b-ab27-40990baa7f1d | -16.90801 | -57.4916 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 0fcb3d7c-d5e5-383d-8f46-f3e0bbd14b3f | -16.90691 | -57.6851 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d524b2fb-8ee0-3bb0-b7e8-5acfbe6007d5 | -16.90582 | -57.50337 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| e445c8ab-efa8-3578-afb1-1607daafa7c7 | -16.90386 | -57.49076 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2f80b7d1-0042-39b6-8288-87f10cad9fd7 | -16.87899 | -57.67104 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 53e6ede0-9cea-3e0d-9bb6-2b4ba33f128d | -16.8024 | -57.64022 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 77acb8a1-d0c2-3d74-bdc3-3ef98c79f4d1 | -17.18737 | -57.29166 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 314b42fd-68d4-3469-ba87-d1ce9f2bf0cd | -17.1826 | -57.29462 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 670d4479-ab15-3210-823c-4005249a8e4f | -17.17736 | -57.41614 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f0be8f5b-b717-3d41-a0cf-e51a17113715 | -17.14272 | -57.46515 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d54a1de6-7c9b-3ec7-ae4f-39c7112f6aa2 | -17.10266 | -57.47313 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c4937ac0-c6a8-3c91-90cf-01a94ec65f7e | -17.08759 | -57.39394 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 22258b8f-9cb5-317a-b353-ad463771ee98 | -17.08736 | -57.41783 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bc034bf5-40c9-3d32-8e01-d10651561135 | -17.08664 | -57.41398 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 3062719b-d713-3b5c-86e6-5cab755aed03 | -17.08594 | -57.41784 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 4e6afc51-56f6-3138-b7c1-b5a3ac7e443f | -17.08517 | -57.42939 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ff6c9639-3bc7-3629-9186-f3fd31a3dee3 | -17.08445 | -57.43324 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 780756ff-f2a4-3256-99ce-3edc003f82dd | -17.08396 | -57.41315 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| f86ac6ba-e6b2-385e-97b5-8acb9dfb6ac0 | -17.08383 | -57.42943 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4318c65f-d087-3d9c-9dad-50e3c6de00da | -17.08323 | -57.417 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 4cf70438-6b28-3ac4-a424-e922c1149295 | -17.08313 | -57.4333 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 64125f18-cfab-3d8c-8a2f-1d4eb4991021 | -17.08252 | -57.41315 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 674f58ee-de02-3b96-8277-75308a165e05 | -17.08181 | -57.41701 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 9d7d89b6-6486-3099-b865-66edd4f931aa | -17.08111 | -57.42087 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 3110d4d4-502a-3ae3-a1c9-6efde328e0e8 | -17.07911 | -57.41618 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| d35bbf29-bf3f-35f8-bce2-e67572d3e6f4 | -17.07839 | -57.42002 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 9a2ae522-8c82-3608-b886-4624e1f2bde9 | -17.07786 | -57.4681 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 04e61805-b0d7-35cc-b575-e30a532674e5 | -17.07769 | -57.41618 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cbd48169-7899-3012-aefe-309137a63cc4 | -17.07713 | -57.47198 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 79185e29-9a15-3dc7-a13d-2689e2ef66d9 | -17.07679 | -57.46822 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0a93f411-6f59-3294-9f25-ed04ad91f767 | -17.07608 | -57.47211 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ea7fc7a9-6296-3e69-85d2-40a006c7a7cd | -17.07493 | -57.48363 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 84f38f9b-1a7e-3d46-9ceb-04231288f508 | -17.07419 | -57.48752 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 0f0699a5-fa5c-3dc2-998e-3f987362ecbf | -17.07396 | -57.4838 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4bcee6e9-5613-35d4-b6ec-a45c81cb68ef | -17.07325 | -57.48769 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fd2423e0-0b9e-3bed-b63a-44cae79baf45 | -17.073 | -57.47115 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9a067d94-0bd8-30c9-97ee-ed99a5451c33 | -17.0727 | -56.87302 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e2533473-0e69-3088-91a1-54c2d2f8a1f3 | -17.07194 | -57.47127 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9d1f09df-08b0-352c-b601-516bc0c3a371 | -17.07079 | -57.48279 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 842f22b8-9bba-3068-bbf5-2b3f53a6e2c2 | -17.07077 | -56.87665 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9effb741-e3ef-3395-9ee9-d484c8894a57 | -17.06871 | -56.87222 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c1186b36-28df-3374-88ba-9d96eecd5f30 | -17.06679 | -56.87585 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 96396382-d1da-3401-aef7-ed8ab053a973 | -17.04578 | -56.85495 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 73dea29a-ff35-3072-941d-041ef07bd2ed | -17.01292 | -56.85398 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 581b1897-78d1-3459-9652-87a8c1a7658f | -16.96412 | -56.82758 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9771e40e-10ce-3941-af48-74742f2be198 | -16.96318 | -56.82607 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 39bf783c-1d02-3ecd-b77f-f46db8e673af | -16.83597 | -56.67809 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a3d49f44-4d03-39ad-ba5e-bd14870de945 | -16.83417 | -56.7106 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 49a1f6ca-ddd3-3d22-9dab-3d3b77acf9bb | -16.83106 | -56.68258 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| dd445fa1-f5f3-3967-b9de-711dfc1a97e5 | -16.78764 | -56.71787 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 68cf59f3-e371-3b97-ad4f-4bd7ce20cce1 | -16.74954 | -56.6705 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 734dd39c-648a-3c17-8fb4-3ff60cc45fa5 | -17.76818 | -57.3744 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 4b759db7-3463-3358-8e45-1b8459467d1b | -17.76748 | -57.37814 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 60451f24-8df0-349a-84b1-dfc7c16b0e15 | -17.76553 | -57.36608 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 40692d4e-f4a9-3818-a402-262eb77a774b | -17.76342 | -57.37732 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| d53ec309-a94a-325a-a850-d48754826fba | -17.70712 | -57.48464 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e8834199-bb61-3da3-b20e-cf39bae7b32a | -17.67508 | -57.47412 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| cbd80c30-5d36-3537-9911-63950da22694 | -17.66791 | -57.42139 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8d899f6b-b877-3cc2-8864-6b1cecb5e077 | -17.66383 | -57.42056 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3634a829-ba10-345f-b572-e07a9f8841c4 | -17.66296 | -57.44796 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 09d68d6b-7073-3b7d-ba85-fdd2c10daf33 | -17.3052 | -57.28741 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4da9dd0a-4235-3cd0-9522-7c4f90f7b485 | -17.30451 | -57.29117 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 84686153-1fbf-3dbc-8dd2-579c40f4942b | -17.30044 | -57.29034 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 787bec90-c648-3d34-a721-b1159d3a6d1f | -17.29975 | -57.29411 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d75432a2-3ac7-3bc5-917c-05b366b6c58a | -17.28138 | -57.30211 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 370cc89d-e96d-3361-ab5d-c613ab29e25f | -17.2773 | -57.30128 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c382c4ad-f3df-3fd5-910f-5f289b5a217e | -17.2754 | -57.26578 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| bbb8473e-49d4-32d4-ab14-248ef23c4018 | -17.27133 | -57.26496 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e5f4fde1-cc3e-3c21-8956-ae3c75788dd2 | -17.26915 | -57.29963 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| dd435533-c07c-3153-bcba-3dd01f9496c0 | -17.26507 | -57.29881 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a9a8e18a-ec84-342a-9c18-b6047279a2dc | -17.26464 | -57.50913 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7ccd197d-217b-36ce-a3c1-d6e667601589 | -17.26393 | -57.51302 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0d74360b-5c81-3ff4-86a2-8111ad28b782 | -17.2598 | -57.51217 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 5184c08c-d089-3873-b3e9-d662611ff9f4 | -17.25908 | -57.51607 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| ffc8329e-b60f-3dec-b2bd-054b4a1690a3 | -17.25567 | -57.51133 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 5850b375-4321-3b63-9b1d-a9f86ac04535 | -17.25495 | -57.51522 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 04001c9a-e675-33a3-8474-2a6719b36566 | -17.25297 | -57.50272 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 74f9a99d-9847-38d7-8b68-701e544afbb5 | -17.2501 | -57.51826 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 10091abb-76d9-3c0e-a837-9632a0959806 | -17.24812 | -57.50576 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| c03f39c2-c784-34e0-b371-10369470a9f6 | -17.24597 | -57.51742 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 03fb3ab1-09c8-34ac-9942-8aae5aa02f84 | -17.23967 | -57.52826 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| d8c30e14-99a7-32dc-95a4-7e9e3814b0dd | -17.23695 | -57.22309 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 517fe051-b771-3168-b3df-be76e1aa3e72 | -17.23626 | -57.52353 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c2d59e25-543d-3240-a803-c3ae5f8df986 | -17.23625 | -57.22681 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 95b0e4a1-3fb0-35b7-bd4b-6a134f6acf8d | -17.23553 | -57.52741 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 7bff4aa8-7f85-3815-9145-e0c8e599f77e | -17.23205 | -57.24924 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 96c56310-5c41-3985-b8da-316ffae0b4fd | -17.2314 | -57.52658 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 17d212de-7204-3712-b1de-bf22b59f1ec9 | -17.23079 | -57.23346 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 8b786e6e-037a-3310-b025-d363a3d011fa | -17.22891 | -57.4938 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f045a1ab-5ad5-3a3b-9720-de9837d467ab | -17.22819 | -57.49768 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5844544a-15f3-3622-9f7f-63012efc5052 | -17.22694 | -57.48133 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 73dbddad-a164-3cd9-90d8-c21a7d268c28 | -17.22603 | -57.23638 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| a2eb6907-d2a3-3dda-87b0-ea0fed293ad1 | -17.22462 | -57.24385 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8f518869-e983-3a23-bf3b-c609ae7f2dc8 | -17.22277 | -57.23638 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |


[Clique aqui para ver as próximas entradas](README78.md)
