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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 104e8e58-1171-3bea-8112-d9a1acf48894 | -1.19204 | -54.21184 | 2024-09-27 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79398d6c-1fb8-3750-90ab-3919255c62cc | -1.19143 | -54.20657 | 2024-09-27 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3b1fd8d-a7d0-31ba-accf-34e192b4f113 | -1.19077 | -54.21062 | 2024-09-27 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3866780d-aca6-3395-bff1-46f04e71516c | -1.18838 | -54.20711 | 2024-09-27 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5100885a-27fe-3d26-9f94-a647d9d01fbd | -1.18775 | -54.21119 | 2024-09-27 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2056fd19-57b3-3b6e-a479-b71f2c6577eb | -1.17821 | -54.15992 | 2024-09-27 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 35d1e651-d8a9-35a0-a318-53c7b92c7d7f | -1.04952 | -53.35952 | 2024-09-27 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e079e98-bb9d-3b6c-b4e8-734cf40f16a5 | -1.04603 | -53.35527 | 2024-09-27 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b70b98cc-0e78-3edd-80ad-7792a8a9b299 | -0.9462 | -53.7296 | 2024-09-27 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 831282a5-8572-312d-8f17-92e4c9de7d12 | -0.94364 | -53.72906 | 2024-09-27 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4791558d-f025-3e05-a812-adb4c1d4153e | -0.94201 | -53.72905 | 2024-09-27 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cde37178-372f-3f3c-9ab6-08330f94f218 | -3.35441 | -53.78038 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 371b6610-148f-353e-9f18-142b1e735451 | -3.35381 | -53.78402 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a341bedd-2519-35a9-9a46-c5b2da163153 | -3.3096 | -54.92867 | 2024-09-27 04:38:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b7934f3-3203-305e-8054-cbbbe84930a4 | -3.64553 | -54.04391 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 67c34c29-32f8-3711-9874-bbc64ac29501 | -3.64144 | -54.04334 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d5a3fe20-2e93-348a-b941-2117e1f5b5ce | -3.63734 | -54.04277 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 30e94293-2fdd-3e22-a7fe-a20fd7604180 | -2.95885 | -53.71894 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b88bb61a-9dd4-3b61-8052-7d6a8b12acbd | -2.94788 | -53.70995 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 307ae466-f16e-3d9f-9609-796e3dab4848 | -2.94153 | -53.69807 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6227035f-64ed-3033-a2e0-8c2b2492ff5c | -2.93749 | -53.69744 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 201bdba8-4872-3016-9c25-50f78d135396 | -2.76653 | -54.76914 | 2024-09-27 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46bb2350-f6a6-39e9-930b-7214c20e3261 | -3.64203 | -54.03975 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8362139-8234-3fa8-97b1-f08bdd565114 | -3.64085 | -54.04691 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fe326145-f641-3dbc-ac90-91e4e58af4c9 | -3.355 | -53.77676 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7298160-1e47-391e-8343-3627ddfa90d6 | -3.35037 | -53.77977 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ecafa76-c56b-3d33-b853-2fb59d6936f1 | -3.34978 | -53.7834 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e788835-f138-378f-9dad-9abb4e5847ac | -3.34574 | -53.78278 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2e98c601-2a37-3957-8532-683b65dba444 | -3.01326 | -54.1331 | 2024-09-27 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58aab935-c07d-382c-9d7b-5e585af39a13 | -2.95538 | -53.71476 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f52a033-1111-3d32-a964-86e2a30d4365 | -2.94557 | -53.6987 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52016523-85d9-307e-b80c-05fd6405bf3b | -2.94384 | -53.70932 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f615391-bfbf-3d87-91d4-c4b022897f89 | -2.76585 | -54.77329 | 2024-09-27 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88947b37-0868-30d2-b393-6a9e8d2cef69 | -4.52133 | -54.84354 | 2024-09-27 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac262af2-399f-31e5-a9d2-feeecfbbb1da | -4.50734 | -54.95528 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 407a1c33-3d30-3a41-8350-2ac2bfac81e1 | -4.50437 | -54.94664 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25227751-ca9e-3d4d-9241-c8bd6e516da5 | -4.5037 | -54.95068 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 367b55d6-82d8-314e-83a9-9dfa101feba0 | -4.50304 | -54.95473 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afd27c99-b878-3f4c-a5cb-1d7da96b35f2 | -4.50009 | -54.94596 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e08932f-4891-3fb6-8bee-f4827dae0aca | -4.48771 | -54.99426 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| befcc06b-0f8b-3f9c-b137-44ea4c7e7b92 | -4.47935 | -54.9385 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69c2eff2-6e7d-38dc-8f37-0393e43f1801 | -4.18113 | -54.42562 | 2024-09-27 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6135c48-2e74-35bc-a4b6-0fb5ad0ee4c1 | -4.12951 | -54.89823 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bf8b52b-d18e-3df5-97aa-bbf8f4a950e5 | -4.5689 | -54.94775 | 2024-09-27 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 64fa0fc2-2e34-3007-9811-5992a5ae2b8b | -4.52068 | -54.84751 | 2024-09-27 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5965a4b-dccb-34b6-b8a9-95f5acf43f54 | -4.51709 | -54.84284 | 2024-09-27 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59b792d4-e0de-3592-bf4f-9b441100caa7 | -4.508 | -54.95126 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe1caebb-f66b-3b45-a226-777fd089ac15 | -4.50696 | -54.87774 | 2024-09-27 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5b17036-282d-32d7-a696-9087383499d7 | -4.49941 | -54.95006 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9c25a6c-469f-3144-a6b7-1e9867b70f50 | -4.4958 | -54.94529 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 498fdedf-9144-39a1-9d0a-c01b4e35dc40 | -4.49202 | -54.99488 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39788bc0-053d-33c4-8b93-c578dfeb03eb | -4.48839 | -54.99016 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fabfaa2b-ae24-3e21-be0e-5fe60c4f33ef | -4.48585 | -54.95229 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1370626e-9c5b-3b88-97bf-ac8e57b25fcc | -4.48293 | -54.94342 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ad6c7d5-f5fe-3ba8-b7f9-49f16383dad1 | -4.48157 | -54.95158 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6ef2d5f5-4a76-34d8-a65e-adab18231771 | -4.47866 | -54.94262 | 2024-09-27 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1df3d6a-cf7f-31b8-85a0-096b98548d4c | -3.8566 | -54.08177 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ebda5b0-fd1a-31ce-a1a9-48c65f906e70 | -3.74683 | -53.86177 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71b25aaa-4a6b-3169-b5cb-78151d5c5ebd | -3.74579 | -53.86144 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 507e5353-8ae1-3b3b-bcc7-d0cd579b9fd5 | -1.74769 | -55.23572 | 2024-09-27 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8417d3f2-ae0e-36da-a256-8d9ba7767c49 | -1.74695 | -55.24035 | 2024-09-27 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ef6e218-787e-34c8-bb99-47f32d4257bb | -1.74237 | -55.23971 | 2024-09-27 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb62a3cf-c9b8-3c21-be07-815124ddeb42 | -1.69997 | -55.00069 | 2024-09-27 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e33c921-a8d8-314e-9743-abebd9561909 | -1.46424 | -55.50489 | 2024-09-27 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed08073d-ebfc-3bb1-97be-4ff3248415c1 | -1.45956 | -55.50419 | 2024-09-27 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ab46266-9a73-3eca-8849-06b5851fd721 | -1.45488 | -55.50354 | 2024-09-27 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 31b9a684-ae16-341c-bdad-dbed872563b9 | -3.58899 | -55.53065 | 2024-09-27 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8781e52-cc51-31d2-92ea-fd74b2dfa1b1 | -3.58822 | -55.53521 | 2024-09-27 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b72544f9-897e-383c-a27f-1873a26ab32b | -3.58706 | -55.53246 | 2024-09-27 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be59940b-7e5f-30d6-a06e-0f15796bc8b1 | -3.58492 | -55.40244 | 2024-09-27 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bf064ad-fee6-387f-b73c-cdea62eb85b5 | -3.58042 | -55.40182 | 2024-09-27 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e06b329c-d480-32d3-a860-68bd7b407de2 | -4.28672 | -56.40912 | 2024-09-27 04:38:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7f60e656-7c60-34b4-896e-9d97060f4636 | -4.28283 | -56.40311 | 2024-09-27 04:38:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 823a3a90-90a9-3f02-bd63-af2a853716ff | -4.28197 | -56.40831 | 2024-09-27 04:38:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e3e28bc1-64a5-34fb-a3d4-8a6d4efb1a59 | -3.84877 | -55.8344 | 2024-09-27 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a03fe663-54e3-3a75-ae13-55def97bd509 | -3.7902 | -55.87629 | 2024-09-27 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e2aa9e8-fc1d-308b-8a5f-0006533002d4 | -3.61462 | -56.80823 | 2024-09-27 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47d74b29-43af-38af-b606-efffd309e0a3 | -3.45321 | -57.98949 | 2024-09-27 04:38:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31b70c81-c1e2-36b9-86e0-b5a15740763b | -3.35393 | -57.93814 | 2024-09-27 04:38:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a72d1247-4d2c-34c8-bf05-38b40aace157 | -3.31268 | -57.76777 | 2024-09-27 04:38:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 494d1174-c5b9-33a6-a2f7-d7b7d3061424 | -3.31214 | -57.77106 | 2024-09-27 04:38:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b33e4dc8-cee0-3388-9117-94b1ff744524 | -3.31183 | -57.76674 | 2024-09-27 04:38:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eb428427-2af4-3182-94fe-dcedbf1a8db9 | -3.31126 | -57.77003 | 2024-09-27 04:38:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad8aa196-e062-3551-b27b-3b8a1d291458 | -2.92651 | -57.84964 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd262e04-d8cf-351d-aeb5-140259895742 | -2.92594 | -57.85302 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cff78ad7-c08f-3391-ad0e-b50953956815 | -2.92538 | -57.85641 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 911eb587-7423-35fc-ae57-cfe5601f338e | -2.92481 | -57.8598 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 233088fe-d27b-337e-8565-44ae8a54a3e5 | -2.92115 | -57.84877 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e95f12d1-8de4-3563-b398-d498e7e8fbdc | -2.92058 | -57.85215 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e65b619e-7466-3f2d-9ea6-200621e64e6d | -2.72502 | -57.50424 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b10e6c3-0737-341e-a999-921e143937cf | -2.72501 | -57.50495 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24610ec6-0e08-3618-ae7a-ec8a77942180 | -2.72448 | -57.50747 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ff3823e-31a7-30c6-a59a-1d68a7031033 | -2.71345 | -57.50972 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 02378bd9-f375-3c0b-9d0c-adac4581137a | -2.71342 | -57.50902 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c44b0da6-e53c-3b3f-bf78-8112f341bd2c | -2.71293 | -57.51295 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3741a050-14ce-3940-abbc-14f509d905e7 | -2.71287 | -57.51225 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 623ac38f-9b3e-30c2-8c3e-f77d127fa0f4 | -2.70542 | -57.52435 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 475fda08-b3c4-3901-ba56-aaf79463ddb1 | -2.68444 | -57.58849 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a2b80315-90e6-3d58-9ad5-4c21be58d3d7 | -2.6839 | -57.59179 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 85e2e94a-03d7-3f8a-b300-6d359ee9e459 | -2.67647 | -57.60404 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README70.md)
