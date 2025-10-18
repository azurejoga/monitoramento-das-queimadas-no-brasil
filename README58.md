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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b746c3a-d36a-3d47-8bf4-2f11ae85e473 | -13.69659 | -47.65521 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 881cb5e7-3469-367f-a10f-4a9e29852949 | -13.40414 | -48.58812 | 2025-10-18 04:32:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b824f92a-b361-3cfd-a504-31ba8a8c13f3 | -13.72642 | -48.11588 | 2025-10-18 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34ef6645-5ef1-3f9e-8f2d-0516d42294d1 | -11.35731 | -44.28107 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85d64514-e8c2-3ff4-a06d-1819b2bde919 | -11.36332 | -47.29594 | 2025-10-18 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59503a21-4f22-35eb-987c-28d046052c97 | -13.04469 | -48.19228 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0045085-4edc-32b7-893e-e98c65d61719 | -14.91846 | -46.71938 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6965b93c-ad49-361c-aec1-13425b7e24a1 | -14.93419 | -46.70631 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a820ac8-c6b8-3f8a-b21b-9482b5e272b9 | -13.45695 | -48.10731 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0a65da8-d2be-3bfc-bc2d-4e994733c6f9 | -13.45454 | -47.92847 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d206052-f0bf-334a-9711-af9803ed6f89 | -11.36273 | -45.26159 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 470d9f59-d861-30e8-b0fa-616d3d809f91 | -11.00293 | -47.90166 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51224e2b-d3ef-376c-9605-b3940dc9b44d | -12.46076 | -45.47067 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd3b81ef-80f8-384b-9911-19fdd45d0965 | -10.88075 | -47.4596 | 2025-10-18 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e7a8e03-59ae-3954-87e1-a885fee675c3 | -12.91129 | -48.57593 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fc79b75-2803-383d-95b6-e9553eae1623 | -11.37419 | -44.29226 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fe41907-ab61-3747-b302-26615e988c81 | -15.78665 | -43.64606 | 2025-10-18 04:32:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00fd79e2-c2c4-3d29-b608-cc8fe93c4e9c | -13.0443 | -46.97113 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb53beaf-88ed-3d3a-97ef-e4056de6a79d | -10.82548 | -48.91379 | 2025-10-18 04:32:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 56169c9a-66b0-344e-ba88-f02c0d919b51 | -12.75451 | -48.63124 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4f6b3cb-7cb0-3050-8e52-2b720481ce8b | -11.4888 | -44.27327 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4727abff-e3bf-3791-9565-f6870663650a | -14.91278 | -46.75663 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b1fedaa-510d-3678-bb77-a47684069815 | -11.61324 | -44.08314 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8baec216-ad07-33ae-8853-e81ab19f1c03 | -13.61192 | -43.96278 | 2025-10-18 04:32:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90c269cd-c9f1-3aae-826a-932e86abe960 | -10.62165 | -48.02082 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15096d1a-6bdf-3efc-89f3-4911330c211c | -14.91221 | -46.76036 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be181787-0f31-3299-8ab6-0ea2e062b4be | -12.91016 | -48.58297 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 26c8d169-5377-3525-9cbb-1c65e2d35a50 | -13.48722 | -47.95935 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c667fab7-5993-3b74-8793-a02a8d8cf4a7 | -11.58397 | -44.05202 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e7271d9-1a20-3aee-bc90-95778cfdd424 | -14.86342 | -52.44239 | 2025-10-18 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7010de2a-6c92-34b8-a70f-dc59c9f6572a | -11.37197 | -44.25727 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e8d6ba7-8427-3fca-97dd-e4e16af420e3 | -11.64202 | -47.86073 | 2025-10-18 04:32:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96f998e0-9310-3d7e-95b9-593784dfb166 | -11.47801 | -44.01596 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fc8f85d-9254-3823-ba77-f936289a6aca | -13.73568 | -48.32869 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b6717d3-f15f-3d09-8b5d-dab3d5e9ff1c | -14.41199 | -49.4094 | 2025-10-18 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8922c397-4f5e-3e83-b653-656e35137425 | -13.4226 | -47.98203 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aca7bf5b-e32d-3072-baaa-9ff48fb92e89 | -12.9651 | -47.94628 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa3edf78-bf4f-3e40-b056-59c7590f776e | -12.91741 | -48.58057 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3648ce8-8ce6-30e7-8694-261db9fb1025 | -11.0035 | -47.89811 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef9530c3-35b1-3baa-9cb1-e9b460511319 | -13.77204 | -48.22895 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21330eda-5875-3b77-b5f8-6dc12e471f4f | -11.40703 | -44.27392 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd4da123-cfa6-3f73-9019-2bbfad5f6888 | -12.93516 | -48.5982 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d54344c7-101c-350a-addf-a528b0dd76d4 | -13.04039 | -46.95207 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8ee04683-2895-36db-84c2-3da5a8ce1ae8 | -14.58483 | -49.07602 | 2025-10-18 04:32:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be6ce4e3-72d5-3cb5-87d5-1f8986c9d044 | -10.70058 | -47.84875 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0884dba3-9284-39a1-bb54-17287b6f6f87 | -14.06186 | -50.05103 | 2025-10-18 04:32:00 | NPP-375D | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a7c5bae-d38a-3a0a-adaf-65a27fe50413 | -16.81412 | -41.2291 | 2025-10-18 04:32:00 | NPP-375D | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 913ec64d-e163-35b8-9cda-49ad674daca2 | -13.44503 | -47.98878 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faebbde2-f3a2-3bab-bbcd-82c913779cb2 | -12.91967 | -41.83899 | 2025-10-18 04:32:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d37a20bf-d732-3f6d-ac1b-501ac42da9cb | -14.86049 | -52.43684 | 2025-10-18 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30c4b7ba-7c79-3346-b28a-290ea190d932 | -15.74986 | -41.91056 | 2025-10-18 04:32:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c124a2b9-e255-31a2-92bf-7110a85dff6b | -13.22216 | -43.9761 | 2025-10-18 04:32:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96d0d2f7-7fbc-3333-8a3d-ea45ecf713d0 | -15.05564 | -46.61021 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d976864e-531d-339e-b8ad-8891d583f725 | -13.04136 | -48.19172 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6732d703-6e1e-3386-bc82-eb0d16bb0987 | -13.70377 | -47.71845 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d2ba3d1-804a-3be7-b15d-133923c2c06a | -12.15812 | -45.06403 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61029f19-1d1e-3143-b7c3-c52882cf5f55 | -14.90598 | -52.40137 | 2025-10-18 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0452a583-91bc-3fda-92cf-fe392b92496a | -13.19994 | -48.31704 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9f9ecbef-abe3-3def-8e50-ed753d68b3a6 | -10.92409 | -47.97616 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93a3d28f-cee2-3be6-baf5-9a51edae7f96 | -13.92445 | -50.2572 | 2025-10-18 04:32:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05a832cc-915f-33b1-a609-bee6e6999e6b | -13.44528 | -48.11632 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a3b6949-52ed-3edc-8fbe-6ffc1fa29b85 | -17.87287 | -45.54483 | 2025-10-18 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c24bbf35-1337-3e63-a65c-0f2f6e5edfda | -11.34758 | -45.26044 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d50e5554-990b-3ef8-8fb9-2ce10e61eb96 | -10.96692 | -47.87032 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a5bffe4-a312-34e5-8434-2c6905eb723a | -12.49143 | -45.50328 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8c04d7f-ea09-3f9a-bd0a-22c8db96fbb6 | -12.4654 | -45.46342 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 95b4c051-2eac-3d3d-85af-8328a233f15c | -12.36816 | -44.08149 | 2025-10-18 04:32:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 352ce1a6-adad-3523-a41f-62cb0dbff04e | -13.22527 | -43.98129 | 2025-10-18 04:32:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8047ee31-5fd1-35e5-b3b1-375638551d7e | -13.02754 | -46.94636 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8b76b39-4432-3c58-972a-3c7fa1502fb5 | -14.90135 | -52.40541 | 2025-10-18 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1efc7ab9-bee0-361e-b371-abd78e5c71cf | -13.03033 | -46.95049 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 728f8f85-c7ba-3a1f-bb6b-3821bde02f76 | -11.85871 | -45.44946 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb8cc08a-b3b9-39ab-af81-15871e657633 | -12.64998 | -54.76126 | 2025-10-18 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 14b07625-c523-3456-9357-17eb4540ed85 | -15.79062 | -43.64664 | 2025-10-18 04:32:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be55c883-f6a9-3c1f-b2fb-3de3e0ae7874 | -15.57576 | -42.12982 | 2025-10-18 04:32:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3421eb36-9aeb-3606-bbe1-ec0caea3cc58 | -14.4475 | -52.89822 | 2025-10-18 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d24074fd-68bd-3d56-8240-452319032fe4 | -11.13259 | -45.84429 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6569f653-b62b-3650-85f0-081cbe48a3c7 | -12.92513 | -48.59656 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4094226f-bf2e-39b2-8999-7d8ee212a602 | -11.00301 | -47.87978 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fc60bac-f301-3ca0-b023-65f2d40a37df | -11.3586 | -45.25812 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6a5793d-495f-354f-8e3f-3b61fd41d0de | -13.86432 | -48.07253 | 2025-10-18 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb63e5e0-3332-31e0-b6d2-456c5f4010be | -13.81076 | -45.51408 | 2025-10-18 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa6a41d8-da74-3319-8005-f3b8b80312ab | -10.53226 | -49.55272 | 2025-10-18 04:32:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87f7979d-7573-355f-854d-61638b128ff5 | -12.36282 | -47.1775 | 2025-10-18 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ec983d3-ff88-35b0-82dd-069178ad7553 | -11.37488 | -45.27539 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 42279750-6161-3cf4-bcfe-2ab94b019600 | -15.51199 | -50.38365 | 2025-10-18 04:32:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5bf0f9cc-4a9d-354d-a185-04fb0aa6d44d | -11.37431 | -45.27921 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44d000e9-61fc-3a11-8212-897cea61ceda | -14.02608 | -44.69024 | 2025-10-18 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69b23ab7-b469-3fbe-9b3f-940da8d77f56 | -14.76299 | -48.19707 | 2025-10-18 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55859f08-dc83-3259-b26d-9d784ae7549f | -11.38349 | -44.25467 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f600278-65dc-3815-9980-aeab88b8f388 | -13.08027 | -43.06467 | 2025-10-18 04:32:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2ef398fc-6459-3451-a0d4-1c06c2d5d7b2 | -10.92985 | -47.55393 | 2025-10-18 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6dea83e-07bd-33fa-96b9-4f129da8946c | -13.2215 | -43.98076 | 2025-10-18 04:32:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 30834416-811b-3956-b864-310baeb10806 | -11.34426 | -44.2183 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5bf9172c-2fab-3d6e-97c5-cfc7a1f50728 | -12.10711 | -45.87865 | 2025-10-18 04:32:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8dfbfb01-9c34-3f53-99b5-3dbddaf47bc5 | -12.45611 | -45.47794 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed40c9e6-8aa5-3cbf-ab82-e4435db87e6d | -11.4034 | -44.27337 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f9f94a7-42fe-377c-990e-057434e16b73 | -10.93206 | -47.5615 | 2025-10-18 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ed988da-5d3a-37d7-9ac9-76e356002c51 | -12.46946 | -45.46007 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 31a7b26e-bb99-34fd-942c-0d2692edaf2c | -12.31195 | -47.83997 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README59.md)
