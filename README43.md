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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccf504e4-b0bb-3d41-9789-09bbe6babd93 | -22.59099 | -48.58414 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e1ed70c9-b5af-31e3-85c2-2038a1532a2b | -22.58492 | -48.57917 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f6a55857-4b5a-3a8e-b8ef-7ce5ed350001 | -22.71775 | -51.39243 | 2025-09-27 04:27:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 27.5 |
| 3ebc1e29-1628-39bf-a24a-740f3c872e49 | -22.21231 | -56.19965 | 2025-09-27 04:27:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 471bd424-6de5-3fb4-885f-0c8d0630e1b3 | -21.00454 | -50.01084 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3c299999-dec1-3262-941f-42695a6acafc | -22.88223 | -51.24013 | 2025-09-27 04:27:00 | NPP-375D | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| c54519c0-df06-39cb-adb5-08abacafc97a | -21.68555 | -45.01812 | 2025-09-27 04:27:00 | NPP-375D | SÃO THOMÉ DAS LETRAS | MINAS GERAIS | Brasil | 3165206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1c8cd62a-4224-3305-9ada-d6b1e94646f2 | -24.55682 | -50.68948 | 2025-09-27 04:27:00 | NPP-375D | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ff4a9fca-78d1-3265-aeeb-db5360881e18 | -22.60823 | -49.02356 | 2025-09-27 04:27:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c321d811-609c-3262-abfc-fbab7a319ab1 | -27.9372 | -51.58306 | 2025-09-27 04:27:00 | NPP-375D | TUPANCI DO SUL | RIO GRANDE DO SUL | Brasil | 4322186 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fd75e180-3db5-3a20-bd65-7998b6223975 | -22.86083 | -51.77891 | 2025-09-27 04:27:00 | NPP-375D | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 30cd4f1b-07a6-3e95-ab7a-d2f9d4649e5a | -22.59492 | -48.58101 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| 3da942b9-38ae-335d-9482-919dfd8c780c | -20.99499 | -50.0093 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b5753606-a52a-3d28-87fa-11edbae20616 | -21.82098 | -47.20293 | 2025-09-27 04:27:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b3240785-8717-38f8-bc8b-a84e5723d7b0 | -22.6049 | -49.02293 | 2025-09-27 04:27:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8da581b4-f24c-315c-8ff5-9921a527b965 | -22.2273 | -49.72763 | 2025-09-27 04:27:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| aa6df8d1-3065-3e79-9bf1-12c8486a423c | -22.88647 | -51.23672 | 2025-09-27 04:27:00 | NPP-375D | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 8ea563b1-af19-3ae3-b771-a076c1cda846 | -22.26386 | -49.56879 | 2025-09-27 04:27:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 98850441-8a4d-3d40-969f-f9b5cdfe764e | -22.58432 | -48.58292 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a7017b68-3a53-3248-9e1a-a1f0990ab4d2 | -20.99157 | -50.00867 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 33347dd7-4969-3287-aa22-12844dabbb66 | -20.99907 | -50.00601 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 898132c7-de1e-35a3-a0ea-3aef86bf377c | -22.71483 | -51.39344 | 2025-09-27 04:27:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 1d51134c-b832-3044-8e37-4ebc020268d7 | -23.02811 | -46.7171 | 2025-09-27 04:27:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 25ed9b54-9e7b-3699-a8c9-14c6604a91e6 | -22.61308 | -49.03613 | 2025-09-27 04:27:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abf61add-01b6-3c71-a5dc-a1ed2672b603 | -22.58314 | -48.59042 | 2025-09-27 04:27:00 | NPP-375D | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| c345f42b-054a-3901-a03a-30d0af125420 | -22.16122 | -52.90321 | 2025-09-27 04:27:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 75cd9568-4baa-3737-88f9-11baa69acb4c | -22.85568 | -51.7871 | 2025-09-27 04:27:00 | NPP-375D | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 1603d2d6-40ff-3691-af91-22d90c114d34 | -22.22393 | -49.72697 | 2025-09-27 04:27:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 401f8e10-08ef-397f-a447-765fadd10d77 | -22.85926 | -51.78786 | 2025-09-27 04:27:00 | NPP-375D | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 31.1 |
| 1125ed2b-669d-3e36-8826-d8fb82ff21e2 | -23.02752 | -46.72113 | 2025-09-27 04:27:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| b1c4c94f-a536-3bbf-9754-703b4e88355c | -21.27209 | -48.33173 | 2025-09-27 04:27:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f754bded-0328-3d3b-83a7-9cbb495cb641 | -23.84753 | -51.7879 | 2025-09-27 04:27:00 | NPP-375D | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 95a3dad0-a669-382e-957a-2eddce05b566 | -22.58941 | -49.05497 | 2025-09-27 04:27:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c644706-6e4d-3f74-ab4c-337b7d300619 | -22.58706 | -48.58728 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 2749a387-1566-31fd-8a5e-b57984c2a081 | -23.67105 | -49.83683 | 2025-09-27 04:27:00 | NPP-375D | SIQUEIRA CAMPOS | PARANÁ | Brasil | 4126603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 10ba4478-5d19-311a-bef2-86acc5b001fa | -21.00183 | -50.01064 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a8df7147-7ca2-318e-902c-4da68370668c | -25.65259 | -52.16205 | 2025-09-27 04:27:00 | NPP-375D | CANDÓI | PARANÁ | Brasil | 4104428 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6764d64c-4323-30a4-8d7d-ad9762f2175c | -22.59551 | -48.57726 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 685122df-3d72-3f14-8dce-33e0e3492788 | -22.71911 | -51.38988 | 2025-09-27 04:27:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| c5c9d1a5-17f8-3fc4-9e69-61a3528a6a51 | -22.88997 | -51.23739 | 2025-09-27 04:27:00 | NPP-375D | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1a0ce971-dc4d-3e25-ad09-70d1d6cffa8e | -20.99841 | -50.00996 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9a96b42a-4d35-3da9-a2a1-bef6180f09fa | -21.24788 | -48.58348 | 2025-09-27 04:27:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4c3b933d-ac07-3f36-9de7-b36ddf670e73 | -22.13097 | -50.01255 | 2025-09-27 04:27:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ed3bf550-ac50-3f90-b3ef-a8676721f549 | -21.00249 | -50.00668 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 59296002-a7a7-3489-8bea-fb38e782c9da | -22.36072 | -49.46843 | 2025-09-27 04:27:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 28622f18-1d2a-3f25-a8ad-0c00004dbef1 | -23.06532 | -47.196 | 2025-09-27 04:27:00 | NPP-375D | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e172ea6b-f3b8-3251-9f9d-1b5be0b2fa69 | -20.99565 | -50.00534 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1a3a97c8-e2ad-3ee0-865b-0b91f8a173ef | -21.81818 | -47.19852 | 2025-09-27 04:27:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| fd873246-8786-3ae0-ab4f-e15facf02bb0 | -20.13213 | -56.85423 | 2025-09-27 04:27:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 893ee16b-29df-3268-b361-dd9e2ea8e9fe | -22.58373 | -48.58667 | 2025-09-27 04:27:00 | NPP-375D | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 7cc80ea5-954a-3243-b848-1c28f36e734e | -22.01978 | -42.20462 | 2025-09-27 04:27:00 | NPP-375D | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ef63f591-fcb0-392d-aaee-de8030e32444 | -22.50039 | -52.98394 | 2025-09-27 04:27:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 4aa016e8-7823-3031-86f0-2c995e3df727 | -22.7228 | -51.38464 | 2025-09-27 04:27:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 5689c9e8-e474-320d-bbab-106daffb1c6b | -20.9528 | -49.61319 | 2025-09-27 04:27:00 | NPP-375D | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c82eb8d6-f8d4-39d0-85f1-74cc1fdc363d | -20.99223 | -50.00471 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 045aa49f-7367-3849-8946-f2b603a07dcd | -22.59944 | -48.57412 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 39c52cf8-e9f6-30fb-8c7c-f992aed461d5 | -22.58158 | -48.57856 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 66c7519b-bb6e-3985-9264-541d880479b7 | -21.48461 | -46.91302 | 2025-09-27 04:27:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8388780d-5901-31b7-9bda-10dcc71bce2c | -24.55749 | -50.6855 | 2025-09-27 04:27:00 | NPP-375D | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b4f225c1-8d5b-3504-839f-e539bc4d10f9 | -21.00386 | -50.0148 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8f5331bd-680a-324a-90e2-d1fee5e8b563 | -22.57825 | -48.57795 | 2025-09-27 04:27:00 | NPP-375D | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 28511282-6bed-34a6-a7f3-c32f3e29e513 | -22.58647 | -48.59103 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| e6e9ae0d-6afc-303f-af1a-b4328181168f | -22.58588 | -48.59478 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 773056ef-7f4d-3fad-bff5-d438c45f178d | -23.03333 | -46.70556 | 2025-09-27 04:27:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c6696ec1-1aa5-3bc4-b252-96854544404b | -22.61702 | -49.03298 | 2025-09-27 04:27:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d5c03bd-237d-34da-9ba8-d8306bdaafe7 | -22.60762 | -49.02733 | 2025-09-27 04:27:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15022279-10e7-3bea-9bc9-bc675c8921a9 | -20.88738 | -56.60501 | 2025-09-27 04:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 580efe40-880a-3517-aac5-58654a691573 | -22.60429 | -49.0267 | 2025-09-27 04:27:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e1ad789-8842-36eb-997e-d19335476793 | -29.95151 | -51.61593 | 2025-09-27 04:29:00 | NPP-375D | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 34fff548-34a9-334e-9ef6-39f0c2c0660b | -29.89802 | -54.66423 | 2025-09-27 04:29:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| 57499641-e3de-3bb0-b931-e35431c11a64 | -31.67992 | -52.35291 | 2025-09-27 04:29:00 | NPP-375D | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 897c8441-9848-3161-a00f-95818a6bca7c | -29.90173 | -54.66513 | 2025-09-27 04:29:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 10ff049e-8d66-307a-b43b-d593d05d3ea3 | -30.39323 | -54.25097 | 2025-09-27 04:29:00 | NPP-375D | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| ba75233b-bca2-351a-b28f-7c64a7fa64b8 | -30.40227 | -54.26325 | 2025-09-27 04:29:00 | NPP-375D | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| d0cd91d7-0745-3fed-a796-25d130abf70e | -0.51813 | -50.90011 | 2025-09-27 04:42:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34fad247-3ef8-3eb9-bbee-147f29814f36 | 1.87546 | -50.84867 | 2025-09-27 04:42:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 789220bf-f46e-3362-a1f9-a5b8dbba480c | -1.78125 | -48.77438 | 2025-09-27 04:42:00 | NOAA-20 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d614873-5f33-3779-9626-a5fe88ef7716 | 1.87604 | -50.85233 | 2025-09-27 04:42:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a053a7b2-4bd6-3f37-a6cd-131bd8e07ab4 | -0.16498 | -50.40604 | 2025-09-27 04:42:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d972645-481c-3219-9651-32473406190e | -1.01092 | -48.96307 | 2025-09-27 04:42:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e842b441-0669-3a0f-a2bb-ee69d1b88abd | -1.14154 | -47.25117 | 2025-09-27 04:42:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ae4e112-644b-3fe5-a1fa-7bd249e08c0f | -0.446 | -52.05909 | 2025-09-27 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d03e999b-caa3-3647-a10f-70e7abac963f | -0.90977 | -47.54516 | 2025-09-27 04:42:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03c1fe99-a57c-3c38-a366-4738ef742089 | 0.59838 | -51.57829 | 2025-09-27 04:42:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac832360-c256-3ed9-96f5-d7d05b4b98e1 | -8.04777 | -46.9059 | 2025-09-27 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 042252d1-75cf-39bf-84fb-c87db807bcce | -5.07814 | -44.85386 | 2025-09-27 04:44:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f5ccd4d6-5cc4-30db-9fee-973d769c4c4f | -7.71428 | -47.30055 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b621892-0e2c-39fe-b978-dc45eedfa872 | -7.71738 | -47.30563 | 2025-09-27 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 63ae3a00-33a6-34e5-9de4-99107abc7002 | -7.27808 | -42.97655 | 2025-09-27 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2b6f7157-abbe-33b1-aba8-c3f8d7240652 | -6.06421 | -44.0816 | 2025-09-27 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c01ddcb-dc96-3a38-9375-ecd3a31992fd | -2.44771 | -49.02518 | 2025-09-27 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91dd3a43-4cdb-3927-85b9-4a67997f1c16 | -3.16133 | -48.606 | 2025-09-27 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd742133-a238-38ec-80d9-a71647d8b9e2 | -6.24456 | -44.09881 | 2025-09-27 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d562b552-6171-33ba-befc-28ca21c289c6 | -3.63861 | -49.16262 | 2025-09-27 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63d218de-673e-3936-b478-f33f4bbd1857 | -7.34775 | -42.09532 | 2025-09-27 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d05e88c8-d312-384a-bbce-033ec4fc265c | -9.18142 | -46.64696 | 2025-09-27 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 484b0148-0594-3faf-aff8-4fafad826696 | -6.2268 | -44.19017 | 2025-09-27 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d54bc02-2845-3ac0-a353-3daeed50c864 | -4.84525 | -50.71294 | 2025-09-27 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83c81ec0-f749-3882-a8a9-f1ebbab00aa8 | -5.08177 | -44.85857 | 2025-09-27 04:44:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e248e2b9-d5bf-3c09-aa39-acbe793d3f27 | -9.00598 | -49.17065 | 2025-09-27 04:44:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README44.md)
