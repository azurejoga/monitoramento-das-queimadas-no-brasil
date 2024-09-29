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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 993a098e-300b-35f3-ba68-def4fbf5c6bf | -13.16488 | -48.55794 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2b1db53-c1e3-38a5-8f58-b241b9e0b536 | -13.16126 | -48.55362 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a619f344-d419-34aa-9ace-1d1acdae7d46 | -13.16076 | -48.55727 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 96541bce-4c3b-3731-ab20-c8fe87806452 | -13.03289 | -48.61345 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 38b5c83c-26fa-306e-bbd0-36f72c1d45e9 | -13.0315 | -48.62372 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc948fcd-817a-3922-8f81-5da4841eda2c | -13.02984 | -48.60509 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1607d615-333c-3267-801c-fe84922f923d | -13.02784 | -48.61984 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eadb76cb-b3ed-3913-9c5a-1c4567f245cb | -13.02737 | -48.62329 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 486ca439-5636-3960-8553-3d62be932e67 | -13.02526 | -48.60803 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9355317d-02b2-3055-9607-c6b037c9795e | -12.75562 | -48.49102 | 2024-09-29 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69f5e563-f278-3155-b35b-da3447bebc34 | -12.75505 | -48.4951 | 2024-09-29 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f20a57ca-f247-353c-9dee-6d5f1f57d6ef | -12.75255 | -48.48278 | 2024-09-29 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb49ac13-0e68-3b31-80d2-efa9bfac8be7 | -12.75204 | -48.48652 | 2024-09-29 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e881cf4-92af-397d-90e7-11f104c1f050 | -12.74888 | -48.47885 | 2024-09-29 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 095d6d9a-6f97-3883-ad3b-732b6d2c65e5 | -12.74839 | -48.4824 | 2024-09-29 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a420e7c5-0d0a-3557-89a9-4580b81698e4 | -12.74789 | -48.48608 | 2024-09-29 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b375007c-4d9a-3a2f-89b5-db69beeada33 | -12.47701 | -48.39811 | 2024-09-29 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed8b645e-60ec-3d5c-9df6-c57446d35ee8 | -14.65332 | -48.82695 | 2024-09-29 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1d41b93-fb0c-31d6-a30e-2083607ed777 | -19.07984 | -50.8749 | 2024-09-29 04:51:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe00e583-e620-31a8-9472-50083887bbe8 | -19.07916 | -50.88004 | 2024-09-29 04:51:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a21a743-d1a7-319e-8d37-2791fbfe5a4f | -19.07597 | -50.8743 | 2024-09-29 04:51:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 0eb570d7-d72e-395e-ab17-372ba4c08513 | -19.0753 | -50.87944 | 2024-09-29 04:51:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 01ce3e3c-89f0-3fc2-b125-6abc71cae97d | -19.07463 | -50.88456 | 2024-09-29 04:51:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2b3d7311-7a80-32f3-85f3-ab8bc6acb4c3 | -19.07278 | -50.86857 | 2024-09-29 04:51:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb0c81cd-85f4-30e1-a65a-fdc720cdec02 | -19.07211 | -50.87371 | 2024-09-29 04:51:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 7d7ad448-a27f-37d8-a9d5-b04a80e7072d | -19.07144 | -50.87883 | 2024-09-29 04:51:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 3b69c5eb-8c96-38e3-887b-a81ffced1582 | -19.07077 | -50.88394 | 2024-09-29 04:51:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 91bc7538-c2d2-32eb-bb3e-34891c41f8da | -19.06891 | -50.86797 | 2024-09-29 04:51:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f2a8593-c0c2-3a1c-889b-110468e6330c | -19.06824 | -50.87311 | 2024-09-29 04:51:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18d6ef3e-0fe0-3ee7-98d8-777365c5646b | -19.06371 | -50.8776 | 2024-09-29 04:51:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 724061da-5a92-3eb1-b4a4-314bf81f1c54 | -18.45946 | -50.25727 | 2024-09-29 04:51:00 | NOAA-20 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1767aac1-6240-3d56-a5ce-8e065cccb089 | -18.45794 | -50.25311 | 2024-09-29 04:51:00 | NOAA-20 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2483e13b-df60-3cc6-b167-d45d0e7d12e0 | -13.55385 | -51.05947 | 2024-09-29 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1cd95b4-ac02-3503-bf46-157cf9f22969 | -13.07502 | -50.85691 | 2024-09-29 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 975d4c46-b5ab-387f-9453-1d7c20aca318 | -13.07141 | -50.85637 | 2024-09-29 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d01e7096-eacc-349a-a560-984bdec04c7f | -12.79322 | -50.61451 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d00f5b2-88e0-3204-bea7-47bd6b2fdb21 | -12.7921 | -50.59676 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92e11322-a0d7-3b7f-9011-173e9b33a3e7 | -12.5473 | -50.63829 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 192cfd97-9a1f-3e79-8c4f-f28b29fee880 | -12.54668 | -50.64257 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03dcf70b-50cd-30f0-9d25-0f1f2b64fa23 | -12.53043 | -50.62707 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00ef91e6-af18-3d8e-acf9-b946a159cf99 | -12.5292 | -50.6356 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e4b9934-de9b-3541-b867-2603df7ecfa7 | -12.52858 | -50.63986 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff9de78f-ee56-338e-a7c8-4f63fc9cc0ae | -12.52619 | -50.63079 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c0c7dc8-d1ee-35c2-8304-5ac9dd92fedd | -12.52558 | -50.63505 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbb693e1-ac66-3e4a-8668-c08f720aa123 | -12.52496 | -50.63931 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f14be15e-d46b-37d0-bb6f-e2e1a2b392f0 | -12.29303 | -50.463 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ba86e74-4062-372f-a4c4-1f6f1d543326 | -12.29055 | -50.50662 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50ff2f1b-c478-366d-8b76-43777a85b23b | -12.28883 | -50.46367 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6dbfdab2-2e5f-35ca-9cf0-452cd10e0525 | -12.28813 | -50.49748 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbd35e5d-07af-36d1-a7c7-753061bdc432 | -12.28752 | -50.50177 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8b0adcd-9a70-3383-87fc-1a0a4d709c05 | -12.28629 | -50.48088 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29e6a480-3b00-3685-ad08-4d1eb69ad751 | -12.28565 | -50.48519 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0f0c5a3-3bdd-3988-8175-138f091695e0 | -12.28513 | -50.46623 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43a1b6b8-1633-30ad-8206-e8f48be8e27b | -12.28501 | -50.48949 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d3e4c7d-530a-3fdc-bfda-594ae4abd3df | -12.28455 | -50.46743 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 460f0c4c-f169-3022-b85f-b5711447a94e | -12.28452 | -50.47054 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fa542eb7-a5eb-3a5c-8483-4417c7492eba | -12.28392 | -50.47174 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7995a505-0103-3d95-9633-74d682e85036 | -12.28391 | -50.47485 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a1f99cea-ec32-3d2a-8050-ccf2f993612b | -12.2833 | -50.47916 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac1e858a-85de-3071-9154-f094f118fa49 | -12.28312 | -50.63623 | 2024-09-29 04:51:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d86045c-5df9-30fa-ab4a-6b99c7607ebb | -12.28269 | -50.48347 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f79c6505-1877-3cc1-bd90-f98447eff421 | -12.28265 | -50.48035 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0af4467-3033-374d-8b21-9d8d92ac3a81 | -12.28208 | -50.48779 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cdf41ddc-4efe-38d9-89b4-c6568e17d96d | -12.28138 | -50.48895 | 2024-09-29 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64d39730-d991-34ac-a9c8-09887ab33529 | -12.27951 | -50.63569 | 2024-09-29 04:51:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be958601-51c3-37e5-9079-e580f01a984a | -12.24117 | -50.66127 | 2024-09-29 04:51:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1c878fc-430f-32d2-8faa-29881819d8bf | -12.23881 | -50.6523 | 2024-09-29 04:51:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6ed9f1d-0473-3ac6-9abe-170d8ca418d6 | -12.23819 | -50.65651 | 2024-09-29 04:51:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1ade64d6-5f4b-3988-a253-d4c949ffd811 | -12.23757 | -50.66073 | 2024-09-29 04:51:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 73993436-2a8a-3602-816b-004b4f63736b | -13.69869 | -50.93288 | 2024-09-29 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76174b37-3d82-377a-b746-f0c5731a42ae | -13.69508 | -50.93233 | 2024-09-29 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 629d81ac-58cd-3979-8057-63c8569734ad | -13.25078 | -51.28166 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2e58f5e-d436-38b6-bbc6-5f43526baa90 | -13.25075 | -51.28253 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95965437-ccd6-368e-9238-8da904c91d95 | -13.2366 | -51.28039 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fb8f169-f014-3a4a-a879-7620b5f8ca10 | -13.23306 | -51.27985 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2ebe767-d5c8-3223-bd10-0851f523ff01 | -13.20778 | -51.23022 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| ef304c15-be63-3847-a1a7-30d90cac0a65 | -13.20423 | -51.22968 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 91a4fae6-fff4-3260-bb23-c3ee4c626845 | -13.20069 | -51.22915 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6737b8ec-5953-33fe-a32b-a3be5d456533 | -13.19714 | -51.22861 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3bc60f6a-64c0-336d-bb12-99324f7789e4 | -13.1936 | -51.22807 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cbf35c9-8f67-3364-aac9-fa194be7d86a | -12.88355 | -51.20163 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d7a1a32-e67b-3375-b6e3-3a9fb5f38436 | -12.88001 | -51.2011 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96b8f136-4b42-37b4-b170-e90e1399f716 | -12.86528 | -51.15311 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3df70ff6-1529-3da5-a585-051cbe3dd16e | -12.86173 | -51.15257 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec11c78b-5eda-3e8f-891e-5543acc46c3a | -12.72414 | -51.94736 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6274f9a3-dd81-36c5-9ecb-c2b77f2a9724 | -12.72358 | -51.95117 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14b83d25-d939-3d5f-946e-fba47c965cf3 | -12.72302 | -51.95497 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b628ae54-0b3e-35fa-a59d-855c7d781791 | -12.72246 | -51.95875 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 285e44a9-4f01-3019-9931-f10c2709e6da | -12.72128 | -51.94302 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ece418a-ad65-3736-9aaf-e06e8e218314 | -12.71859 | -51.93903 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1809f462-d7f6-3c5c-a99d-7424cda4c9b3 | -12.71841 | -51.93867 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88f37ccc-5a2b-38f0-a3de-8833eb013fbf | -12.71289 | -51.93033 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 932f73b0-2635-3f7c-85b1-9365287e60a2 | -12.71062 | -51.92215 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57417b53-30dc-3740-a778-0625e7a34393 | -12.71004 | -51.92597 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3978f148-6e21-33b6-8270-c7a7a67b0104 | -12.70834 | -51.91396 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25b5e4a4-9168-3783-af34-d370f215d0d5 | -12.70777 | -51.91779 | 2024-09-29 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 342b2461-7f3c-3c64-b5e3-9c46b0186f13 | -13.77223 | -52.42517 | 2024-09-29 04:51:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c157fdb0-3d2e-3fc7-a16b-4697c3f4ddff | -17.67172 | -53.10317 | 2024-09-29 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b870fe98-77af-32a6-9b5c-d1c064ab9371 | -17.66829 | -53.10262 | 2024-09-29 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f154de71-9bca-3c71-b4de-2e2d55086ac4 | -17.66145 | -53.10151 | 2024-09-29 04:51:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README56.md)
