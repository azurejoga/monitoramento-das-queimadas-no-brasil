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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a27297e8-73ef-326a-b12b-680a30c39f33 | 4.27179 | -60.0369 | 2026-10-08 05:21:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9be683a2-8a89-3926-9db8-5546a4870974 | 2.43665 | -50.81658 | 2026-10-08 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 82fc13da-33dd-3502-9f36-7d0650de88a6 | 0.69989 | -51.43165 | 2026-10-08 05:21:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c8b5cac-2c5e-30bf-8148-1d1017348cfe | 1.76969 | -55.54813 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1eda4128-90fb-3494-8116-6e96f251d9a8 | 1.95031 | -55.13082 | 2026-10-08 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ed0cb15-fa8c-38f7-a005-9eef85172483 | 2.44056 | -50.81596 | 2026-10-08 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99f71a51-fa01-3317-bb70-f358749d9129 | 1.68901 | -55.63485 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2434ae1f-7be2-3e49-969f-92bfb6196ad1 | 2.45308 | -50.81896 | 2026-10-08 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd78ad4e-36a2-321e-bc2b-b1b72df2c2dc | 2.12544 | -50.82253 | 2026-10-08 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed08075d-98ff-3788-b865-bc57bb61c735 | 3.74235 | -51.62043 | 2026-10-08 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 91db6d0f-4180-340a-89a1-c1a03cdccbde | 1.74527 | -55.58729 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a1bda81-2b9c-3b50-a6fd-e450c7aac1ee | 3.54053 | -51.27453 | 2026-10-08 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccfdc266-b396-3196-a961-d485624851fb | 1.50344 | -55.7069 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20f4107b-c948-3903-b6df-329bc3202c42 | 1.74805 | -55.58332 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d62c7dde-1e6b-3cdb-b53f-65df75796f9b | 2.11431 | -50.82624 | 2026-10-08 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1eac6a80-55f7-3143-8efa-2f3b75fd6ff6 | 2.12215 | -50.82497 | 2026-10-08 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d92a1ce-3ffb-35e3-bca2-8f596f534a2e | 2.43338 | -50.81886 | 2026-10-08 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bc8d78a1-3003-3798-8687-6b4b06993179 | 2.43437 | -50.82699 | 2026-10-08 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42d871c5-9c4e-332e-ab38-d2b3e296a11c | 3.07156 | -60.55836 | 2026-10-08 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02e5eb15-d53a-3413-a43e-f88536eac081 | 1.70205 | -55.61526 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6d8c008-b323-364d-80b8-0e1c24b8edae | 1.70428 | -55.60784 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1252827d-f42d-3b6e-abfd-3b33c3dc736f | 2.32574 | -50.87344 | 2026-10-08 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c80f060-4748-3445-9936-4cf09f7becb3 | 1.70482 | -55.61129 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b995d7f1-37e0-33f0-baca-fd89b8e76971 | 0.70263 | -51.43341 | 2026-10-08 05:21:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d12c1153-7ddf-34d9-bcac-7e9218e6acda | 4.42574 | -60.91124 | 2026-10-08 05:21:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce047320-be6d-3b5d-95ca-56f5fb16e8e8 | 2.1075 | -60.62341 | 2026-10-08 05:21:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfbc8b16-16f4-3b12-87e9-67d7eed900dc | 1.98859 | -59.93707 | 2026-10-08 05:21:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 530e208e-5c4b-385b-bc1f-f2c8c805f24e | 1.6566 | -55.79553 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eec401bd-8ec2-3542-b3ef-d1965feb8f65 | 2.43416 | -50.82376 | 2026-10-08 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5bb2bd79-0b2f-3cac-8a79-6b8e24007002 | 0.69878 | -51.43403 | 2026-10-08 05:21:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ae59d0f-2402-35a4-8e54-ae1b5127c204 | -0.09025 | -49.4825 | 2026-10-08 05:21:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69e280bd-41db-3a78-baf2-3f7a88f8b2e9 | 1.71315 | -55.59939 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71f3c0f9-491a-37c8-a3c2-c6f3d32a92de | 4.3116 | -60.35702 | 2026-10-08 05:21:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59e8486a-9cd0-3e1f-9b7f-0c038ecca1ee | 0.56217 | -50.79655 | 2026-10-08 05:21:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be115eb8-90d1-3090-91b2-a0e3128b0e5a | 2.11117 | -50.83182 | 2026-10-08 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65f13349-5a6c-3d01-85a0-a91ce4166c36 | 2.12607 | -50.82432 | 2026-10-08 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ed8753e-9b77-3e33-b46c-7869a2f17e20 | 2.00037 | -55.87321 | 2026-10-08 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 051fd483-b938-32b2-974e-717dfc47b2e2 | 2.1145 | -50.82938 | 2026-10-08 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46778afb-81bc-3ba3-a27f-73f84d18750d | 3.16274 | -60.59161 | 2026-10-08 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7c95301-bbd2-36a5-898a-5ebb6aa93827 | 2.1176 | -50.8238 | 2026-10-08 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a04f4c3-45b9-39b3-a5aa-605a1d363ea3 | 1.68678 | -55.64227 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0173b70-8883-385b-a369-19197a34d141 | 2.90688 | -60.94447 | 2026-10-08 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73f1b0ac-a11c-3a5b-b2f5-5cf66f24a9f1 | 3.54126 | -51.279 | 2026-10-08 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4d90539-29e1-33bd-816d-c7adade5a555 | 4.68805 | -60.57109 | 2026-10-08 05:21:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04a1e23d-73c1-3405-afee-6545c481c55e | 1.31809 | -50.84865 | 2026-10-08 05:21:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 903ee928-526c-3695-951d-5db5d0b7134b | 2.43746 | -50.82147 | 2026-10-08 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d2903f08-1e0f-3b95-acbb-d6e6df1c8880 | 3.1232 | -60.64321 | 2026-10-08 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0305b85f-6481-329a-90e6-749c8828d244 | 2.90628 | -60.94053 | 2026-10-08 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee1b8988-f427-3924-8ed5-717363da2706 | 2.54485 | -60.61033 | 2026-10-08 05:21:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5dfe999e-5649-3b04-b1e8-19dd3d718f49 | 1.72034 | -55.6018 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a873c90a-1ada-3c11-8495-38ceeb871550 | 2.11058 | -50.83 | 2026-10-08 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c35c30b-968b-3bd2-8c97-79a5d9115903 | 4.26772 | -60.0377 | 2026-10-08 05:21:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f1fc324-5d47-3086-a891-861dc48b7556 | -2.95525 | -54.10275 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88091760-63d8-3e6c-bbe0-99d42166bd64 | -2.50352 | -56.12502 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d08134a9-daaf-328e-a333-171cb54e4c8f | -3.07915 | -53.95833 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4d80c324-a1ab-3b7c-ba55-d76073d1964a | -12.20085 | -57.12981 | 2026-10-08 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dde828d-d77e-3f38-a11c-bcd018fb871a | -6.11427 | -51.73411 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71f519b6-e8e3-358d-9b6e-7052e34d67a4 | -8.6202 | -67.05875 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cd1bdf2-4621-31cc-b0d2-a26f4b6fbc02 | -2.93514 | -53.93216 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79833f69-b25a-380e-8f2d-31acc979b5b1 | -2.77241 | -54.07237 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9145fd3b-9f14-3961-a5c8-ea353deaaa94 | -3.26559 | -54.03325 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 804e87a3-0f69-3de3-83f2-0e66f3b68d31 | -3.0535 | -53.91409 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 409eddb2-704c-3797-b73c-85577d17e633 | -3.66691 | -54.50568 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fa7a3ea-4627-3db1-8ee7-9a428d438698 | -3.30498 | -54.0353 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 85d62c81-a71f-36d0-b01c-7a03a84e369c | -2.85413 | -59.26145 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89063b50-3384-3318-97e6-3411d69d49b3 | -4.81578 | -54.74185 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f8a84dc-57b9-3635-a8d2-01de000e5eb5 | -6.17056 | -51.93777 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ce50330-9fa5-308f-8a27-b05c8d8e3db8 | -6.1358 | -53.07245 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61ee8007-46a1-3419-aec2-307f7d39121b | -1.21342 | -55.64226 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d309431-82a9-30be-931c-9f668900e760 | -3.27758 | -53.81618 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3806ee6-3ba0-31d9-b43d-bd073acde631 | -2.87968 | -54.17374 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c6f4c40-214b-3ff6-8af3-dc416ca4cdb7 | -7.22516 | -55.16833 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ffa3992-48ef-3e0d-af72-1567186b2777 | -6.1487 | -52.64268 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d242794-b563-3ac5-9a36-7a3069285741 | -12.10676 | -57.17593 | 2026-10-08 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fb70170-7377-3982-820e-37b2ce3448a1 | -3.00994 | -54.74996 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd242978-b61c-35e3-98c6-b8a480fecde8 | -3.30004 | -54.06659 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba618d10-f3aa-3f9b-a756-bf5976d62cef | -2.95724 | -54.15825 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7d2a277-fd35-3eb5-969e-f0aa1bb76480 | -3.00839 | -53.90332 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c0223a0-4339-32a4-9412-b1ac940023ed | -3.59962 | -54.57265 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b2589ea-6d1d-3aa7-858c-cb8c90ab2a59 | -3.59536 | -54.6679 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f666cdcc-c2de-3730-90b8-38f7832323ac | -2.89694 | -56.67561 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3a04034-933c-3393-a8c3-591583793d52 | -4.26564 | -46.39894 | 2026-10-08 05:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 408ff0fb-cd79-3dec-95b9-9c82bc00f34c | -5.2934 | -60.09528 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a71f76ad-7000-3b73-8286-3470d7a8245a | -3.66706 | -60.62731 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e272140-36e5-350a-b669-f6483c6b437e | -1.75499 | -55.12135 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbd0ccb5-9eb2-3ec8-9ca5-45096f5b928a | -4.2162 | -56.05191 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6fd62bd-660a-35b0-952f-b163c58a8e70 | -6.11847 | -51.7346 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a414734a-24f7-3dd8-aecb-4c5eea51bfce | -3.08454 | -53.94704 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9c4d4a31-b022-3068-a2de-5a9e2908e83b | -3.89953 | -58.9522 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23b4fa1e-e6c9-3eef-abe8-63eb921646fc | -3.03157 | -53.93887 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e63e97a-24fe-3ee5-9603-38af893312ce | -3.58905 | -54.6631 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6a2f7461-828a-3b33-97b6-e734f3fd2659 | -3.43606 | -56.9414 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7abaa3fa-25e7-3e6d-8898-b6347be93b32 | -3.10122 | -54.2776 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 560dff3a-26e8-33d8-b935-ca57611f476a | -3.66858 | -60.61814 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1618ea93-bbea-3cc9-8dff-755b64e0d780 | -2.83548 | -54.13255 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2d70f7e-78e3-34d7-8ee2-c2ea4f84a202 | -2.47353 | -56.09906 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58819f8a-37c4-3406-91f6-10dfacfbd7f5 | -1.3024 | -54.20555 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d80141b-d557-3afb-95d4-22eff9409bbb | -2.39333 | -57.89367 | 2026-10-08 05:23:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7e4b2ad1-c12f-3c48-aa5a-d019c99e8692 | -2.52475 | -58.09667 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4a25d6b-fc0f-3c96-a9de-988ac7f983a3 | -3.87105 | -55.99451 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README124.md)
