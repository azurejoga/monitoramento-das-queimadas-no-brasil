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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8963620f-175d-3a0e-bde2-c7640b5d342f | -13.8112 | -45.8057 | 2025-10-08 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| d38a4375-b6fb-314c-abd1-48b92152b122 | -14.7179 | -46.0867 | 2025-10-08 13:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 441.1 |
| 012b30f2-c57b-3e09-885c-895444fe8751 | -14.8634 | -51.4804 | 2025-10-08 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 226ef6b8-0138-34f3-9f8b-a9d3203e72d6 | -11.6701 | -50.9641 | 2025-10-08 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8a51a8a2-5c2b-390d-b0b4-763e32af878e | -13.3967 | -47.2382 | 2025-10-08 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 7165e4ff-eaa0-30aa-9ee0-6d09be0e1b32 | -12.7825 | -50.5112 | 2025-10-08 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 76e06d9b-ad9d-3467-8019-c4aa57674714 | -8.1007 | -39.4489 | 2025-10-08 13:20:00 | GOES-19 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 2f9f453b-03c1-314f-8ad0-bd6d7d89ce01 | -12.4916 | -54.7364 | 2025-10-08 13:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| d4af7306-d920-3986-801a-bdae5cd6ef28 | -9.3343 | -48.9364 | 2025-10-08 13:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| d75923b2-ffa8-32e9-b604-83ae2860cc92 | -14.211 | -43.4573 | 2025-10-08 13:20:00 | GOES-19 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 2a77ec55-13a4-3078-ad20-6b56a47a8986 | -15.6195 | -52.5928 | 2025-10-08 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 305.7 |
| 6768eac4-6b2c-399b-ba3f-16cd20d15b7a | -13.8536 | -51.8504 | 2025-10-08 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 3d91547e-d33e-3e33-ab48-4e0719c38ff2 | -8.8618 | -46.0949 | 2025-10-08 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 8f83305b-e71a-3941-b77b-0c17c0aa430d | -7.7919 | -44.246 | 2025-10-08 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 191.0 |
| f330f22b-7ad1-31c8-9fb0-602185bec383 | -10.1874 | -45.9889 | 2025-10-08 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 25e62565-a502-337d-8e59-6bc7fb3775e9 | -12.1083 | -50.914 | 2025-10-08 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| f5d244ed-3ac1-3cb7-9ef2-0f8f923bdf5d | -13.3018 | -47.1626 | 2025-10-08 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| d8d4aa74-faef-3ee5-a7bc-6e6539d73d7e | -12.5107 | -54.7345 | 2025-10-08 13:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 6cbcc9cb-a0f7-3704-a0fb-2020ea4544f9 | -18.6147 | -44.4479 | 2025-10-08 13:20:00 | GOES-19 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 4934bd80-2750-3387-9ccb-9cbf9ba2845f | -8.9495 | -46.6013 | 2025-10-08 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 2aeeaeda-c1fd-3696-9622-a23039060da3 | -12.1576 | -51.4399 | 2025-10-08 13:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 68e540b5-4c04-39f3-8b2d-e24deaa2d2da | -15.321 | -46.1622 | 2025-10-08 13:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 9f262402-a8aa-36b1-a6cf-6c7368243936 | -12.1646 | -50.9714 | 2025-10-08 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1f0ed792-dfc3-33f3-8a4c-a94a13633f39 | -7.9085 | -45.5145 | 2025-10-08 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 13250de7-9841-36a2-8266-2b7f0a0c677f | -11.0262 | -50.9067 | 2025-10-08 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 23523419-dd3a-3284-bce5-f57ccb138173 | -13.3438 | -48.0072 | 2025-10-08 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 7491f671-969b-38cb-a405-30750380edfa | -15.6198 | -52.5715 | 2025-10-08 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| d6ecc5ab-1569-3478-b3e0-0230fd86493f | -8.5398 | -46.2181 | 2025-10-08 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| b41546da-80b7-3f45-9d24-aef8b5f94cf9 | -7.7932 | -42.6082 | 2025-10-08 13:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| b9be249e-85d7-3983-b3f0-ab0747cd696a | -11.1292 | -47.7526 | 2025-10-08 13:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 24bdd36e-778f-371d-a69c-6071ac3c0754 | -7.8307 | -44.1497 | 2025-10-08 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 25c211a6-e87a-377a-b434-38e9f01f95aa | -14.7379 | -46.0601 | 2025-10-08 13:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 10e2e8a5-c02f-31b1-931d-5e9e61b026dd | -17.954 | -44.4124 | 2025-10-08 13:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 101.7 |
| dac9858f-2597-371e-a927-723dd9a3e85e | -8.4824 | -46.2912 | 2025-10-08 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 18fb3eba-67c2-3911-beb6-1f0ed913bc4f | -13.2855 | -48.0381 | 2025-10-08 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| f06d2dd8-b2d7-3b0b-b565-4c109db993f9 | -10.4251 | -46.591 | 2025-10-08 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 966c151b-5da3-37c1-a484-f8d4d9112b6f | -9.6795 | -49.9355 | 2025-10-08 13:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 88f22106-dccc-3bc2-81d5-0bd3886f69a7 | -14.3889 | -46.0063 | 2025-10-08 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 112.9 |
| c20a8926-6235-3071-b38e-a1b74c995f86 | -8.691 | -44.727 | 2025-10-08 13:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 7a7780b5-e5e6-3d9c-b027-37a6f0e92bbd | -12.4916 | -54.7364 | 2025-10-08 13:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 47b12a55-415b-3b46-8b3b-1ba7c222895c | -10.4245 | -45.3907 | 2025-10-08 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 626.8 |
| d27809eb-55e5-32a4-9a60-facca4f030b7 | -8.8621 | -46.0724 | 2025-10-08 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 5a49d16b-46c8-3aaa-98fc-7924620c0f9f | -11.6851 | -46.382 | 2025-10-08 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e1cd48df-edc1-33eb-96ac-47260af220bd | -12.1652 | -50.9287 | 2025-10-08 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 77ffe446-6532-3190-89ba-c37438fdd433 | -14.8835 | -51.4346 | 2025-10-08 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| aaee1c9e-5ba0-37b0-9ec6-a583e6945051 | -13.8117 | -45.7826 | 2025-10-08 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 1eb87190-4ba6-3e0c-b74d-593c1db47c83 | -8.8618 | -46.0949 | 2025-10-08 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 36913155-c514-347a-a640-b0861a8b7a34 | -10.0504 | -50.4113 | 2025-10-08 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b143a796-4b81-38bb-aa57-7233e86c3e05 | -11.1482 | -47.7503 | 2025-10-08 13:30:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| a25be700-90b5-3dda-819c-06e05a0698a1 | -9.6607 | -49.9373 | 2025-10-08 13:30:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 0a749ee9-288b-3f8d-8920-c942b1530460 | -13.3774 | -47.2411 | 2025-10-08 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 4b17c087-0fa5-35da-a215-f27b94dd4125 | -18.0209 | -57.5214 | 2025-10-08 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| cd033d82-f393-34e0-b437-56eae0b7d2b5 | -8.6295 | -45.1 | 2025-10-08 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 300.9 |
| e7027650-4959-32c5-8c73-07639a015016 | -14.8832 | -51.4561 | 2025-10-08 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 8a20d0ab-f9a9-3ffa-8461-03ba8710d166 | -14.8828 | -51.4777 | 2025-10-08 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| c8abf245-2fe1-3ace-9aa3-cb3ddc3f9ae1 | -15.3979 | -48.0164 | 2025-10-08 13:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 07cdd025-96ef-3e3e-b649-3b6d755de2bb | -13.8112 | -45.8057 | 2025-10-08 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| eb683117-43e8-3595-95f3-9a5aca0881d7 | -8.9121 | -46.5829 | 2025-10-08 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 5940592c-d1e6-3359-ac0a-edda2e49cc39 | -8.5393 | -46.2631 | 2025-10-08 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| f389b3e2-9a16-31c9-bf02-5919300eaabf | -10.1874 | -45.9889 | 2025-10-08 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 7b2bde64-13f7-3485-be02-fe28d2b53554 | -8.1993 | -43.3424 | 2025-10-08 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 366.9 |
| 1caaa5df-fda8-351b-ba07-5e2144593bac | -8.5584 | -46.2387 | 2025-10-08 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 4501f48d-6c2f-3a07-87f8-03110a7a8b64 | -8.9309 | -46.5809 | 2025-10-08 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 233.1 |
| 72f57e48-7f25-39da-a113-f8be11d45dc9 | -7.458 | -47.1861 | 2025-10-08 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ed77de9b-31c7-34f2-8f4c-94245a3d1aad | -7.7922 | -44.2229 | 2025-10-08 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 197.6 |
| fb37688a-3924-3799-a71d-943468f13dc4 | -9.3343 | -48.9364 | 2025-10-08 13:30:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 771b8975-f650-3640-8573-8f77c4688740 | -8.1804 | -43.3445 | 2025-10-08 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 267.3 |
| 5b7f4489-e782-334a-b3a8-d82ce89a3d95 | -11.6701 | -50.9641 | 2025-10-08 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e85c14a0-3193-3752-ae15-bba4bb7056e8 | -12.5107 | -54.7345 | 2025-10-08 13:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 8af85578-003b-3cc5-950c-060119298fea | -14.4079 | -46.026 | 2025-10-08 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 4fe25aac-c9f5-3c09-8bf6-5e9ea324a383 | -14.2559 | -45.8681 | 2025-10-08 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 3d0db6ff-3efc-3ce1-a2cd-b7d907a8ebcf | -14.3884 | -46.0294 | 2025-10-08 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 96.1 |
| f19062bf-9b01-3a48-b667-bbb9d06d4911 | -13.3018 | -47.1626 | 2025-10-08 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 95af3282-af4f-3270-a018-e8f119412c1b | -12.5297 | -54.7326 | 2025-10-08 13:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 484987ad-1528-34b4-a520-721eeecee7c2 | -13.3706 | -47.6013 | 2025-10-08 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 41b511b6-2485-3c9c-a320-f585e1b62106 | -12.2525 | -47.8728 | 2025-10-08 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 3d9bd378-e466-3e03-9cb3-6063b60eef7c | -7.6193 | -39.9576 | 2025-10-08 13:30:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 76.5 |
| af9f2039-38a2-32ef-8e45-daf32a54cf8d | -10.0506 | -50.39 | 2025-10-08 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 4e9afb64-f10a-357b-bb4c-230c1884a1fe | -12.0314 | -45.1901 | 2025-10-08 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| c381d0c1-6ec5-3f67-b172-bee01996705a | -7.7924 | -44.1998 | 2025-10-08 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 54390c6f-c221-3459-8c1a-6d87ff9e2fe3 | -7.7203 | -42.4023 | 2025-10-08 13:30:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 5f762c30-e45c-380b-be18-13635477b1a7 | -8.1007 | -39.4489 | 2025-10-08 13:30:00 | GOES-19 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 98.8 |
| c6959338-0a89-36f2-acf2-2a4434e3c16e | -12.3809 | -50.5393 | 2025-10-08 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| ef602b93-8a73-3212-9e92-b5082565929e | -8.6106 | -45.102 | 2025-10-08 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| fcbcae95-829a-3203-a53f-71e1174a925f | -13.3778 | -47.2185 | 2025-10-08 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 6cb66034-53d8-3a1d-8295-ca0d517026e2 | -12.0122 | -45.1929 | 2025-10-08 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 3ba1b918-4c2d-3172-84b7-3e9f010dc5de | -8.9005 | -46.0233 | 2025-10-08 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 9b9cab14-f762-3ee4-9224-35558febc228 | -14.8824 | -51.4992 | 2025-10-08 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 704c931d-198b-3f04-8fea-d81127eebd45 | -8.1807 | -43.321 | 2025-10-08 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 185.5 |
| 368cb700-4493-33f7-affe-af7df9c475bf | -11.9523 | -46.4126 | 2025-10-08 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 79bbd08a-2a25-30d6-aef3-af53b7c6345f | -14.7179 | -46.0867 | 2025-10-08 13:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 214.2 |
| 79a1f34a-49df-37c9-924e-1ed3b88b339c | -12.5109 | -54.714 | 2025-10-08 13:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 5fff6b3d-f1f7-35c7-81e8-e38828f952f8 | -14.9022 | -51.4749 | 2025-10-08 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 0dc3ac8c-b9f4-3da6-a206-6859b43294be | -15.6393 | -52.5688 | 2025-10-08 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| d462a29b-0e44-38e7-9c09-8eb9fe4ba7b1 | -13.3513 | -47.6042 | 2025-10-08 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 00118c6e-49e0-36be-aa9a-79bc0098a5b8 | -8.199 | -43.3659 | 2025-10-08 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 3915cfbe-eed6-3038-92c3-4a371c3adab0 | -13.7923 | -45.7859 | 2025-10-08 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c09d05ea-e27e-30ff-8a42-da2206bd2fc0 | -7.7919 | -44.246 | 2025-10-08 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 280.9 |
| 4922cbe5-049e-38a5-ab28-de70341731eb | -13.2847 | -48.0827 | 2025-10-08 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 07fefc8d-e944-36ae-a8dc-ec980d0bd4b3 | -16.0754 | -45.7634 | 2025-10-08 13:30:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 118.5 |


[Clique aqui para ver as próximas entradas](README105.md)
