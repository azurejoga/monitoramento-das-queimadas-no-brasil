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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d2f7f64-dd21-3ee1-9217-e98eaae2f78c | -13.37793 | -47.31423 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7242d605-2ffa-36fb-9a5a-e4ac9eb925b7 | -15.99872 | -50.87674 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 518b691a-2cad-39da-b25a-a36d21fdcc46 | -13.30993 | -47.22684 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b70bd61-3a8e-3068-968a-40eeec05d427 | -10.57074 | -57.81627 | 2025-10-01 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddb89fc3-6831-3fa3-859d-fdbd679a5fec | -14.05354 | -47.97081 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8996e382-90dc-3ce9-a4e9-10374ef224a9 | -10.90618 | -46.50803 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3c212dde-e327-348f-8064-21e06b62bfaa | -11.75879 | -46.85967 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbb3114a-3c86-349b-a678-8c8d4edcbf69 | -12.4476 | -50.18372 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b1cf61d-2226-39c5-aa1d-c4734999f6e5 | -15.17843 | -49.08156 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9eb82d88-bb73-378a-9dd9-433e3c46fb13 | -9.44668 | -50.89765 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f7d50b5a-6b9c-3656-88b4-fc6027b88bb2 | -11.06399 | -47.82313 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 26c407eb-0807-3f69-8e2b-a1b13ebe0bcf | -14.49998 | -48.44716 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 074d89cb-bb35-34a6-81d6-442ea4679271 | -16.38351 | -47.05037 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a37b0670-6683-3a63-b498-f22982dedc47 | -14.35046 | -47.13547 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc3b96cf-2e65-3714-a5e9-6b6b0a8284a4 | -11.1376 | -43.38207 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f6f592b2-a878-39e2-830e-44465b002acc | -15.27334 | -49.28085 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 926ec975-a9fc-3f10-8f55-bfd9832b831a | -16.39342 | -47.04256 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d65d5ec9-324b-3ddc-aa85-a31185847a97 | -13.55153 | -47.27557 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9d395bf-a543-33ee-821c-1b932cd405a1 | -11.82178 | -44.96289 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b0215c8-af65-3b24-8bc9-d5e6bc617c94 | -12.75934 | -46.88663 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3e0b60b9-bbd6-36ed-80b7-ed6c4228a3c9 | -10.6238 | -48.59282 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e31984ff-cfa6-3215-9f5c-ccb640231612 | -13.67556 | -46.79198 | 2025-10-01 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9833952f-0c05-3e72-9403-70b958e304c9 | -12.36854 | -50.2043 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5057cc49-d8f5-3fce-83ec-1dea2a89e731 | -15.49517 | -45.9162 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c414620-d546-3065-8b74-504a5bfec653 | -14.4975 | -48.43654 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a74cdd3c-3efa-389f-9344-9d578579a2eb | -12.94356 | -48.4183 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eced51e7-15b2-31bf-88da-79ae313e828e | -15.1702 | -49.08508 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6922730f-b06b-385f-ae7b-709b8272b48f | -13.94321 | -48.12434 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 10c08904-a4a7-3d04-b249-378d730a9772 | -10.90583 | -46.57037 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f5c36255-f5c0-3725-9e12-89ded9f343ce | -12.17486 | -51.4127 | 2025-10-01 04:51:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad62c0c5-5010-3966-9907-fd77249fb95c | -14.70222 | -48.22144 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b74f99c-ae05-3e4d-8bba-fd175e433f49 | -8.96804 | -50.25051 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c3597ba-e55a-3036-b19e-e765d17e8cd6 | -15.60864 | -46.90692 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e91bbb28-5dd0-3e46-aaf4-b0c2def03287 | -13.28822 | -47.2316 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94def8df-3c60-3bba-92cc-99025c0c5e45 | -14.54488 | -48.24204 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef742246-1dca-3d74-96e8-9f774d1cb1b0 | -13.22689 | -47.32485 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88efac86-248e-3357-807c-74a85b1ff565 | -13.72017 | -54.71823 | 2025-10-01 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67b2a472-69d4-3c45-90e0-c36f9c7a42b8 | -11.9669 | -46.59624 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 094db3a5-9eb6-38a1-be57-8a9edd010ada | -11.81166 | -44.96676 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6272544b-1819-3266-b674-89ecc679ba3c | -16.40594 | -47.04894 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e1d3c16-2f20-34d9-a601-0d850aa662eb | -10.06556 | -48.19342 | 2025-10-01 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f0dd9de-b49c-3bd9-98d4-0d96d62fbacc | -12.15038 | -47.76868 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dee6903b-7754-3c45-9c50-2632cae3c087 | -13.36849 | -47.29143 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a68cb8ea-29fd-39ce-851f-fc3630534c95 | -16.11779 | -48.40056 | 2025-10-01 04:51:00 | NPP-375D | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6490a852-2261-3de6-ae18-2da82b237958 | -10.48437 | -55.58207 | 2025-10-01 04:51:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5b12b7e-4ae3-3619-8b75-865acd70d435 | -13.80259 | -47.48596 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eca5680c-9996-3d4d-81f4-505f053b7cdd | -15.38157 | -49.19387 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 911fbe76-1aee-3e0e-b015-b20928fd596e | -12.88541 | -44.68315 | 2025-10-01 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6748aade-bfe9-368d-92fc-404e5649025a | -13.06898 | -47.06499 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a56f1639-7eb1-3853-bdf9-b39b4cf1e71d | -12.7824 | -46.87468 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2856418-d3a0-3641-88e0-5bbbb5a341a4 | -11.47062 | -45.09035 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fe0a0b5-b90a-30a7-b14a-9cee14c6c894 | -14.18035 | -46.1181 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b5f7346-97fc-3308-aba5-f0d5c2d8c4b0 | -13.20915 | -47.33212 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97fadc2f-da57-3798-a587-814adb5c4713 | -13.91373 | -48.08676 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c809c26-983f-3d19-8dec-731cd7c0d17f | -16.36133 | -48.15778 | 2025-10-01 04:51:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 128a8cca-a205-3042-a8db-5e13529006c9 | -14.06251 | -45.04124 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ce8d58cf-f442-37f7-a2a7-e47c265cd22b | -11.6224 | -52.24566 | 2025-10-01 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84527e75-692c-3c46-957c-8ce306e38684 | -16.08624 | -51.03978 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f12b101-5d27-3a6f-b68c-639108252c63 | -15.38534 | -49.19445 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c6f3f6b-7b9a-3f84-8ab4-0916ff7b7ac2 | -14.50809 | -48.47517 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0dfe9ed6-87b5-385b-965c-4fb6894f1e70 | -12.85228 | -47.01972 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 405db41a-8999-376c-b4ae-7e6aa19672a2 | -14.59033 | -48.2229 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 897e0c07-d148-39e6-aa6c-268c19d817fb | -14.03606 | -47.96394 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdc14d24-1061-3860-8325-a37abbbdb610 | -14.95179 | -47.50938 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a48af88f-4f36-398b-9ce5-dc558d92d382 | -14.89955 | -51.67176 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8c2fa17-ca95-3839-a294-3b7bd36390a2 | -13.66406 | -48.07722 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 764402f6-da26-3a2d-9611-637c850c2c08 | -12.87579 | -46.94203 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ec44374-86f3-37ac-af3a-0ef1ca9cd056 | -15.66101 | -51.33383 | 2025-10-01 04:51:00 | NPP-375D | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0fb6482c-a392-3362-a6e9-31e46d087565 | -11.27255 | -47.81218 | 2025-10-01 04:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 347aa45b-3c59-37ba-a526-70f794d83ffe | -11.63104 | -47.49052 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 253558bd-abd9-35a9-a2d5-af27c84d9a1b | -10.73872 | -45.37692 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| effe3ed8-56e7-3369-8035-5fbd0bde49a3 | -13.14037 | -47.41708 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bae9b5dd-9277-30d3-9477-be288fb4cb3a | -14.9914 | -46.95486 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abb2ad3a-d4f7-3e49-a6ef-d68efddc262a | -14.51519 | -48.47996 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04af87da-9972-3cba-aac6-bb7506a3a10d | -13.37182 | -47.32791 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 241be132-af6c-3c15-96d0-5da4378cf640 | -13.71609 | -54.72145 | 2025-10-01 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d18cfbf-f983-3d2d-9ffa-77790546ef08 | -15.83474 | -46.25481 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c1aa96f-adb2-347d-85f3-65501f960b3f | -15.99928 | -50.87292 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b077f7e-bc9c-3868-ae4a-72d558e5edc9 | -14.52379 | -48.36313 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 738bed91-76cd-3ddc-8be3-071ac3fc683e | -15.69024 | -51.27958 | 2025-10-01 04:51:00 | NPP-375D | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0b700d1-e83e-3a2f-a05a-7a089015de3d | -11.39872 | -44.89518 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12421f8d-3662-334a-bc96-19d17d7a1e92 | -13.32497 | -47.33315 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f2064085-82d9-3241-91ea-d136d8bd5ca6 | -15.80409 | -43.32035 | 2025-10-01 04:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de8e0b7a-ff9e-399a-82ee-061a1c69bb99 | -13.93085 | -48.09696 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13d2611d-3f7b-3d3d-85ac-d30097840b74 | -9.42474 | -54.71252 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 463773d0-a823-39e4-80f0-82ee1ea452ae | -14.86973 | -56.44794 | 2025-10-01 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 54febe35-1660-3663-a0cd-6576ae080ef2 | -13.56273 | -48.06018 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24e9c337-8b99-30d1-8ef4-d692a6189f61 | -12.22768 | -43.75267 | 2025-10-01 04:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5892108f-a3c9-3ecc-8b6e-c47c7ca8c639 | -15.33986 | -47.84108 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72b6ce2e-ede9-302e-b0bb-499a799c76a2 | -11.42484 | -43.50172 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e09b000-7a38-35b0-a95e-601a6e120926 | -14.17585 | -46.1174 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23f5d0a3-f871-3a01-85fe-8b3b39e1be85 | -10.90709 | -46.56537 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d86482df-8a08-3709-9420-ea70b3d8140d | -10.21881 | -43.04162 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1fedb60e-6c2f-3712-842e-a2985af31dc9 | -14.89999 | -48.37568 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e8b17e3-f9be-3279-9e3a-8e63d2e6f210 | -14.6838 | -48.11824 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 60d901fa-9547-361f-ad27-0903603685ab | -11.66744 | -47.49135 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0bd0cf60-a47c-3058-912a-ed61095ac055 | -14.90318 | -47.20657 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dead0296-3735-3907-b2c0-bb677b192dbd | -14.75412 | -45.77216 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27ade53b-a152-3018-a74b-19856460f97a | -12.85801 | -46.94708 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 734618bf-dbb9-38b1-9172-897c7883d6e7 | -12.17983 | -45.04385 | 2025-10-01 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README100.md)
