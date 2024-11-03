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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b12e686b-ced2-3c7c-9a5c-b153a2b68c48 | -1.19123 | -53.69205 | 2024-11-03 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e5828bc1-9ba3-3757-b18e-9ee8110992f9 | -1.18889 | -53.68262 | 2024-11-03 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b00e400-d81b-3195-8249-2e9894cba34f | -1.1882 | -53.68705 | 2024-11-03 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb409c0d-1cd6-34e2-9f07-5c74c8237b4b | -1.18751 | -53.69144 | 2024-11-03 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 141bb690-6a0e-349e-ae0e-5e86e3626d71 | -1.18586 | -53.6776 | 2024-11-03 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e87fb3cd-3f3f-3b3d-a0b6-953e83740db3 | -1.18516 | -53.68205 | 2024-11-03 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4c22fe81-4f6e-3a67-af9a-c73da8644be5 | -1.17697 | -53.68543 | 2024-11-03 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4dd36dc8-7a8b-3f84-84a5-ac3c09f25f58 | -1.14673 | -53.37801 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 431ea6d1-5650-3dd7-b482-a4dbf0a67a33 | -1.14368 | -53.63045 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ea3a5aac-0cba-39c9-910e-ae9f9335c120 | -1.14217 | -53.62765 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52288cdf-5df5-3685-83c8-cc0f9d0e8bd7 | -1.12626 | -53.43672 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f309e6c7-8453-30cf-80da-e963203f2c71 | -1.09633 | -53.6525 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3531c84a-f478-3712-915d-ba92750376a6 | -1.09331 | -53.64738 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad1e26d6-a400-35ab-8e5e-59c393817bab | -1.09261 | -53.65186 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ebe4068-edc6-3fe3-8fc9-68aa5ab2b8dc | -1.08958 | -53.64676 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e1acd47f-6130-3e12-b492-3797444a0674 | -1.08889 | -53.65119 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 706c26b8-ce5b-3ec4-9bc2-ffe485e10fcc | -1.0882 | -53.65562 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e21e3492-e495-358c-80b9-f0abf291328e | -1.08585 | -53.64618 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 846b597c-11e4-3940-99d0-b90218b69ab4 | -1.08517 | -53.65057 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f8a5894-70bc-3ec3-b0e2-026d92149532 | -1.08143 | -53.64999 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb4242ce-f27a-33ab-ba43-b39f57d5cec5 | -1.07769 | -53.64948 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1791e6aa-65ef-376b-b4d4-1c5b4202e697 | -1.06661 | -53.36128 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdc69703-6945-325e-b7c5-0bdd5026579b | -1.0306 | -53.72905 | 2024-11-03 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3dc476fd-e771-33c6-a380-467a8d7149f5 | -1.02315 | -53.7276 | 2024-11-03 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00b06282-e039-3282-a095-399c121ccd71 | -0.97822 | -53.71325 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8f20d04-db69-30eb-a011-3baa4e43e3ec | -1.31784 | -54.21951 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a721c033-bbbf-38d0-ae47-23acc8788ca8 | -1.314 | -54.21887 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ff76218-1ecf-3f3d-8dd1-abc190d705d7 | -1.23913 | -54.20446 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1634191-c8c9-37d7-b2ac-91e31045328d | -1.21746 | -54.16679 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e6e78c9a-e753-372a-bb16-9dbfe8a1216b | -1.20599 | -54.01674 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fd92b5b1-4d0a-3201-89be-a216f8f04f78 | -1.20526 | -54.02128 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ff33943e-1b85-3520-b1ab-42c88cafbf90 | -1.20221 | -54.01601 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b312f3f0-4fc1-398b-9cf5-61ec0c97807f | -1.16885 | -54.17529 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1ae1511-5413-31ba-a9d9-53166e139b3e | -1.16808 | -54.18007 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| deb49499-dfb0-3dab-a89c-40b04c17dbbb | -1.16648 | -54.1766 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e93b3614-9d8c-39af-a38f-6e6513550815 | -1.16423 | -54.1795 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5551bf95-049d-3b07-ac9c-821d5e97f880 | -1.16192 | -54.07885 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2ef172dd-6a48-311b-8c98-cbb384268dd6 | -1.16119 | -54.08356 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6867aa19-8747-38aa-9368-5214aecdbd45 | -1.16046 | -54.08826 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 422765d8-b4dc-3466-a66a-4f89f3a39e2c | -1.13457 | -54.10349 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bb12b44-49ec-320e-b039-feec45880a91 | -1.12171 | -54.13546 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0108fa87-fb74-39b6-a018-1a6829647233 | -1.11863 | -54.12997 | 2024-11-03 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33ebe9ad-670b-3b48-ab63-a7131b4d6528 | 1.72586 | -55.91036 | 2024-11-03 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b143955d-8bc8-3945-939b-dde38e3029dc | 1.71999 | -55.90194 | 2024-11-03 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a65f0b4-f380-3812-bdbc-50e2ab9194d0 | 1.71931 | -55.8974 | 2024-11-03 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0488ec91-b725-314d-ae96-430e703d7dbb | 1.7172 | -55.89701 | 2024-11-03 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d519c3a4-7e8f-3946-92a6-acfefd71bc09 | 1.62779 | -55.91494 | 2024-11-03 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8b8d12f6-d2eb-3c0b-bac5-af3edc1bf151 | 1.62396 | -55.92013 | 2024-11-03 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6b2ffdf2-3e0f-3046-a0af-cc1afd751403 | 1.62014 | -55.92536 | 2024-11-03 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7f31830f-1222-39cf-9f0b-ca00a59995f8 | 1.12981 | -59.44443 | 2024-11-03 04:44:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bc23399-7d68-37ae-bb0e-23456da17fb6 | 1.12919 | -59.44043 | 2024-11-03 04:44:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 692cbc8f-6865-3890-9739-7e1f3387cdce | 0.68044 | -59.80902 | 2024-11-03 04:44:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 583afd6b-f1b0-3e8e-9cdf-2b5cfab970e5 | 0.68004 | -59.80992 | 2024-11-03 04:44:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f916fc1b-246e-3960-adf3-f0fcb92916c9 | 0.6794 | -59.80589 | 2024-11-03 04:44:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54fd9763-d10b-3c98-9140-37ce3fee4e87 | -2.28658 | -46.80489 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8faa4ac9-7a12-39f8-9c2c-99c6772e8417 | -2.28424 | -46.79596 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef520af7-55f7-3527-9b7f-4a6c4ad0b2f0 | -2.28359 | -46.80014 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6adf755d-bc2d-36c1-b408-d931500c5d60 | -2.27736 | -46.81643 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f96896d-9e2d-34fe-97fc-e274958f60db | -2.27373 | -46.81585 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c128d21-cb2e-3fe7-b5e8-253c531210b6 | -2.27308 | -46.82008 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29962236-75c5-309c-91bb-ebbd328b7313 | -2.26945 | -46.8195 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88071263-454e-3d1c-acb3-1ad31a15118e | -2.25445 | -46.86873 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a62a0104-7503-312e-9f21-1738cb7ca068 | -2.24598 | -46.80295 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77469444-f6b7-3bd6-b20c-ac61190ce5f5 | -2.24235 | -46.80239 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37d6fa77-688c-3d13-97f2-353816732c7b | -2.2187 | -46.88464 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2bb7674-5995-3f34-9106-dcee217fcc10 | -2.21508 | -46.8841 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c461e92e-04f4-3fc3-995f-5b0d5f4d1ecb | -2.42765 | -45.71333 | 2024-11-03 04:44:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ad40cff-444c-3ecc-a526-35c93d0e4c65 | -2.07997 | -47.12962 | 2024-11-03 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da44305b-668c-3903-9610-4af7fb675e75 | -2.0764 | -47.12907 | 2024-11-03 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31e687c4-0281-3b7b-ad5c-4644542ac1cc | -2.07578 | -47.13312 | 2024-11-03 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e523cb0c-76f2-333f-92ef-cd516a642046 | -2.07284 | -47.12853 | 2024-11-03 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cadaec3c-0748-3c0a-bff7-871397aa0e73 | -1.96776 | -46.82903 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f114dca2-3932-36e8-8eed-0832f544cd2e | -1.18288 | -46.91081 | 2024-11-03 04:44:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 07629fda-6199-3edf-9716-bb352c6378b2 | -1.17931 | -46.91027 | 2024-11-03 04:44:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07ed76a1-120e-345d-9ba7-9ceccb0881e0 | -2.16049 | -46.38783 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed662d3c-dbd6-3319-b14d-a7efca3adf3d | -2.15857 | -46.38991 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a4588af-890d-348c-87d5-7ef04f501229 | -2.15678 | -46.38728 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84cd4085-4728-33c9-995d-70af0c1e7f5f | -2.13823 | -46.3844 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71c80b1b-4d94-3ae2-87e3-54a147ade397 | -2.13452 | -46.38383 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 069a0ffa-6efd-30b5-abce-fb49182eb5b1 | -2.13142 | -46.67009 | 2024-11-03 04:44:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80b37148-2681-31d3-8f5f-508f796baa97 | -2.12956 | -45.98933 | 2024-11-03 04:44:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 753307f4-286b-3f84-b190-0aca45842e7d | -2.12883 | -46.68718 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3813d5b3-33c8-365b-a31e-fe94efad82ba | -2.12712 | -46.67379 | 2024-11-03 04:44:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 395e8503-2979-3d90-bea3-5f371382e15c | -2.11023 | -46.39363 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8062e3b4-9bef-382f-bd7f-34cc7e59e5bb | -2.10955 | -46.39804 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53ed25ed-042d-370c-ab49-0c15cd121879 | -2.08192 | -46.38025 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02d5ba0e-3f37-3e00-a7d9-704f31e44eec | -2.07986 | -46.34373 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 77f804a8-3a0c-395c-b0bc-efbef2d6575a | -2.06298 | -46.35478 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 254fe179-330f-3976-960f-44cb2cd813ca | -2.04536 | -46.44666 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 296e8f88-3325-3fbc-a510-bde6d4df51cd | -2.00832 | -46.59295 | 2024-11-03 04:44:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fe0503b-60c2-36c7-8cc7-e9e275625c35 | -2.00765 | -46.59723 | 2024-11-03 04:44:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74fde62a-3d3b-36b4-9383-8e541c1405ce | -2.00466 | -46.59237 | 2024-11-03 04:44:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c953e55-ed44-323e-8d4e-a052a3a0969a | -1.83638 | -46.05532 | 2024-11-03 04:44:00 | NOAA-21 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e3c42cc-db43-3a7f-8c95-cafab678c7e2 | -1.81209 | -46.03761 | 2024-11-03 04:44:00 | NOAA-21 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09377d3e-c041-323c-817f-e1e41c01f159 | -1.74784 | -46.07583 | 2024-11-03 04:44:00 | NOAA-21 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9728b4e0-199e-3f74-867a-be643a1b31fc | -1.74643 | -46.0849 | 2024-11-03 04:44:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff0a4116-c709-3d23-b096-5d46cb2f1bb1 | -1.74337 | -46.07982 | 2024-11-03 04:44:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e991863a-ec1b-37df-88cf-26f3f5ec4ef8 | -1.74267 | -46.08434 | 2024-11-03 04:44:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7b82c86-3e18-3aed-8344-3a0b0cdccbae | -1.74032 | -46.07468 | 2024-11-03 04:44:00 | NOAA-21 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 914e5c8a-e06d-33a4-960a-73355d5006d8 | -1.73961 | -46.07926 | 2024-11-03 04:44:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README35.md)
