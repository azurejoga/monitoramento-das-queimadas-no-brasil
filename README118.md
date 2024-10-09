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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c19cb8dc-bdba-3090-a62b-64e68844d199 | -7.30222 | -44.98096 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0d1fa34c-9803-37cd-a48c-d9a49e7943dd | -7.30023 | -59.73766 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 288952bf-1d1b-3b34-b85e-42c2bb21add9 | -7.29959 | -59.73801 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3fe38d5-99ab-304f-a895-d034ddff6ebd | -7.29949 | -59.7417 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d9db8b1-0c8e-3cd5-be65-698c41d762d3 | -7.29888 | -59.74206 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af93cd72-18ea-357b-a38b-c67fa2c6b7cc | -7.29449 | -59.73674 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d734900-3ae7-33e8-b90d-f569ac733593 | -7.29438 | -44.9798 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90beb9e5-e26f-31fb-b585-3cfd2529644a | -7.29385 | -59.73709 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d964933-ccd6-3e0c-aa8f-999f2889354f | -7.29374 | -59.74077 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2187729e-d292-3a29-8cf2-713cff2f2429 | -7.29314 | -59.74112 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1cefafb-73e3-3108-92c3-8584f5b2603e | -7.26657 | -49.48697 | 2024-10-09 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b92a146-e607-32e5-8ab2-6d361e4c26e2 | -7.25838 | -46.33741 | 2024-10-09 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bc1d74c-22a0-3041-9992-3df7e198a13c | -7.24872 | -59.62723 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7d25ad2-8afe-3678-b0b2-b53bb1bb0b91 | -7.24799 | -59.63131 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bbd3132-e677-3bfb-82fc-cec01c68013f | -7.2423 | -59.63028 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebcf5531-0bc8-3488-b456-3027857aa69b | -7.21011 | -51.6802 | 2024-10-09 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9869c398-44c6-37cc-a2ab-c4cb4c57711f | -7.20333 | -47.6966 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fca2a7b-d460-35be-9a49-a8abb61fd7e4 | -7.20276 | -47.70028 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ba35e7f-1b62-30e5-bb75-9a2229aa4b5f | -7.19225 | -59.77512 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e4f1cc0-69b6-3a28-a7bc-de0acaf16389 | -7.19154 | -59.779 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 34f08116-86cd-3910-b592-a2b3c4e7bbd9 | -7.19077 | -59.7832 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eaea15a9-e4ee-32a0-adba-58ceff54dc03 | -7.18649 | -59.77416 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60367a24-731a-3fda-a8bf-34d1e3fa495a | -7.18576 | -59.77811 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b7d0ca3-fe37-3048-a84d-851cabe916cd | -7.1856 | -59.77551 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99cdc774-b445-31ec-9c6a-24e96213d2c6 | -7.18501 | -59.78222 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d9504f5-7a8a-33f2-ae55-1e8b800dd870 | -7.18489 | -59.77952 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c0bbd5a-6a36-3086-b9a5-9ad80fa72bea | -7.16154 | -59.35451 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b1cfef03-6b96-314f-bb38-92e41b530e25 | -7.16084 | -59.35835 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5a6cd796-5665-361e-a9bf-b6e66c9aa9c3 | -7.15069 | -49.44729 | 2024-10-09 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e2861ec-b0a8-3459-8a7a-a95d535c9f6d | -7.13911 | -44.83696 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a2006b4-5320-3ba2-add2-fd9065d65f8f | -7.1368 | -44.83494 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6161c737-f829-3e55-8906-8ea815fd3ad9 | -7.13519 | -47.8219 | 2024-10-09 04:38:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fbc9c87-f28d-3bfc-9f91-e0fe4469038e | -7.13462 | -47.82564 | 2024-10-09 04:38:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfa2e0ef-9dde-363a-8133-9563927cb0bd | -7.13333 | -59.30087 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21fbfa4e-3237-3e1b-aa0b-31bc602443d7 | -7.13268 | -59.30458 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae751d87-5276-3115-902d-be16b00b3913 | -7.12775 | -59.29988 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f99b9c92-971c-3252-a22f-25aed3cea58e | -7.11925 | -49.86283 | 2024-10-09 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e83566e8-acbb-34f9-927a-fa35f83a8744 | -7.1161 | -49.15295 | 2024-10-09 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccb249a8-30a7-3d04-b421-fd4b190768d2 | -7.11592 | -49.86231 | 2024-10-09 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8c824b14-13b9-3576-a5ae-58b3ab42f0c4 | -7.11555 | -49.15643 | 2024-10-09 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d0dc5dd-0097-3330-91f2-96ffbf9a5578 | -7.11537 | -49.86578 | 2024-10-09 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfb8ee69-fed4-3fc6-9142-50befa7f4e96 | -7.11204 | -49.86526 | 2024-10-09 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb94cd5e-f9f5-3bdd-bc13-6c34a9e8511e | -7.10005 | -45.26973 | 2024-10-09 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbf2d4e5-1af3-35b5-a1de-3b1f8a9e98ee | -7.09805 | -44.46163 | 2024-10-09 04:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1eef9fe6-53c6-3bf5-a1f0-cd3d16f87592 | -7.09732 | -47.86542 | 2024-10-09 04:38:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d905979-84d4-358b-9e02-a15370666eb2 | -7.08937 | -47.87177 | 2024-10-09 04:38:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3eec1687-f0f7-362d-a26e-c65f1abfbdf4 | -7.08652 | -47.86767 | 2024-10-09 04:38:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed3ef821-40f3-3e6f-b8ab-3d2f2a45375f | -7.08256 | -47.87077 | 2024-10-09 04:38:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60fb5729-8763-320d-8ae3-70e223cde332 | -7.07074 | -59.45696 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8abdce30-7ca3-39af-b6b1-eaae78298f50 | -7.06562 | -45.45123 | 2024-10-09 04:38:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72a8a3ac-36e0-33c5-8439-ae8f23943737 | -7.06511 | -59.45594 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e901695-f600-373e-97b5-2f3554b549b5 | -7.0466 | -48.05812 | 2024-10-09 04:38:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b44f33b-3143-3323-b75b-32494b6f7ac3 | -7.04604 | -48.06173 | 2024-10-09 04:38:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22433e9b-e682-3fb9-a1e7-da3ebc22b0b6 | -7.03121 | -59.41824 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1da8d835-ba17-340c-9b19-df0da89b8472 | -7.03081 | -59.81108 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b55fa728-3524-3c2d-9903-e7e5639cf004 | -7.03008 | -59.81516 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b6b8573-be41-3cd0-9c86-a70aefb62abf | -7.02908 | -59.41437 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b17ddf4-90bb-397e-bc18-38db768d8ee2 | -7.0284 | -59.4182 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1d5fe83-fdb0-3fed-9dc3-77675d603438 | -7.02773 | -59.42202 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 416ebdb6-4523-39c8-b471-f3a03c824b0b | -7.02707 | -59.42583 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ba9b684-7e20-31c2-b4f8-f48ae35b228e | -7.02558 | -59.41724 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1432e558-c92d-3440-bd0a-e125211344c1 | -7.02489 | -59.42105 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fe7872b-83bf-3d44-9075-5c44d1e4b848 | -7.02419 | -59.42482 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 455acdfb-77e9-33fa-b597-7ecfe59073cf | -7.02344 | -59.41338 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc58a351-c029-34a2-bdc8-e8c41618148e | -7.02277 | -59.41718 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4973cd02-8291-391a-8781-1deb1aecf05d | -7.02211 | -59.42097 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36553c25-affd-3bb9-9d17-5bb1ffd3d75e | -7.02145 | -59.42472 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be0547c7-9168-377b-bb17-b2f2c07adff2 | -7.02135 | -59.40866 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a2ee8a2-1979-3470-a9e5-10aa32e9ea05 | -7.02065 | -59.41246 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c5dbc8d-1d61-306f-b05a-02c1633d562f | -7.01995 | -59.41623 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 219b35f0-3c28-3158-9331-fa8045ca4195 | -7.01926 | -59.41999 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e328699-767c-310d-9974-1265188cc334 | -7.01857 | -59.42375 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e898f151-f696-35f7-8700-5d9d6af7455d | -7.01781 | -59.41236 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b5ea185-d0a4-3521-b721-f3e5268d80d4 | -7.01752 | -48.54249 | 2024-10-09 04:38:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6ca21b2-e6a4-39b0-b379-810cfb3df24e | -7.01715 | -59.41613 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b2f27d7-1e6e-32b9-abe1-636829c11bd7 | -7.01698 | -48.54602 | 2024-10-09 04:38:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8518a015-72d5-3406-9ef2-e5f82938ea90 | -7.01572 | -59.40765 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b38c8bff-a6fd-33ff-a7e9-c88cfa28e2cf | -7.01502 | -59.41145 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fbd33558-cde3-39e6-83e1-4ade559d489e | -7.01418 | -48.54197 | 2024-10-09 04:38:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 937c5edd-b59b-336c-a34e-1c8936f2caf0 | -7.01286 | -59.40754 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a65d4d6-bdef-3685-a8d6-238105c5445c | -7.01248 | -47.37079 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a9bd079-91f5-36a3-9ad7-332f90d945e7 | -7.01218 | -59.41135 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3988860-1a7b-377d-beee-ace13f230ad7 | -7.01083 | -48.54144 | 2024-10-09 04:38:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3dfb958-a322-30d9-ab54-4655ff18bfec | -7.00903 | -47.37022 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 578707b3-0573-3244-bc11-054fd65f759f | -7.00662 | -55.32987 | 2024-10-09 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 943f30e0-2fb4-3bd7-8967-2285aef5317a | -7.00234 | -55.32917 | 2024-10-09 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e98768c2-6174-3244-be94-ac38596def8a | -6.98717 | -45.3858 | 2024-10-09 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 462aeb3b-40fd-3bce-889b-1135f317d449 | -6.98405 | -45.38056 | 2024-10-09 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 142956be-98c5-387d-8ce4-73695f5a0825 | -6.9652 | -47.3906 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99d85082-6d1e-3c9e-a334-0c02eef82826 | -6.96405 | -45.27735 | 2024-10-09 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91f61734-2127-36b0-8b9a-a2bea04b8e98 | -6.96361 | -47.39011 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19ce04dc-dad5-376d-9334-9e7aa14cfcbf | -6.96216 | -45.27485 | 2024-10-09 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e1fecd5f-fdfd-30fc-92e0-fd7ba911c009 | -6.96176 | -47.39004 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7ab591b-cbf7-3fb0-ab65-37f044d83cc0 | -6.96021 | -45.27682 | 2024-10-09 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 772cbc5c-8187-3fcc-a259-e12584580d72 | -6.95833 | -45.27428 | 2024-10-09 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c9d8caa-a087-3d13-ae70-7a62edf1e496 | -6.9462 | -45.22476 | 2024-10-09 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8c17fde2-c906-3932-bf33-8884549b9a92 | -6.94331 | -44.61765 | 2024-10-09 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2424e5a-8bd3-32f4-aadc-7abe746f8651 | -6.94152 | -44.62027 | 2024-10-09 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bd50c2d-db4a-3e06-b5dc-769eaaf2ee22 | -6.93931 | -44.61712 | 2024-10-09 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 360c5c6a-c215-3198-a046-6acbdfa9a9cc | -6.93747 | -48.17403 | 2024-10-09 04:38:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README119.md)
