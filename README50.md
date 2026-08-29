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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81ace7f1-e31d-33da-8493-fd7da337dde2 | -11.02805 | -57.21611 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c24d73c3-067b-3ae5-b97d-33e65d49d7e8 | -19.28484 | -49.51805 | 2026-08-29 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3b5d457-6bd2-3c0b-87b3-7e34a42ed88d | -12.2027 | -50.54559 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 076dc991-5151-3473-8a35-a7476c0ce529 | -8.96088 | -50.79883 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4bb5a3c-f3b4-3f0e-aa30-cbaf7e5251df | -8.82645 | -49.6435 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78ae5cfe-00ff-385a-bd5a-73e8687e88fa | -11.0281 | -57.2501 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c0f2cd4-fa9a-356f-a5be-c059e147b97b | -9.43361 | -51.57553 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49650c7c-eb08-38fd-9985-4b0786733826 | -8.58978 | -54.76643 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82fd5243-6d51-32c5-9699-54e3acaafef5 | -6.765 | -55.65999 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38f2c08b-3336-30e6-8bec-7352016f9635 | -11.26766 | -54.03282 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f5b4229-cbd0-3821-969a-74985ac9b4e8 | -11.72131 | -54.53534 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15317d7c-c652-3fcb-a837-58c974da74f2 | -8.94643 | -50.80377 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ede01e2d-2542-34eb-8b0c-fcbad5f68118 | -10.33743 | -49.97238 | 2026-08-29 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaf02281-934e-3b6d-86a8-09567ad125b9 | -6.77661 | -55.66162 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| a288fcf6-bff2-317c-873d-11922d79b681 | -6.76806 | -55.66536 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d31d24ee-08cb-3b39-a051-05059175124b | -16.47497 | -49.24057 | 2026-08-29 04:53:00 | NOAA-20 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91380f6f-8730-3625-8d5b-7748624ddad8 | -5.88147 | -57.77467 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f60a764f-7522-3c8c-971b-d0dc5dca88e8 | -7.28136 | -49.96757 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97b2dff0-f059-3a22-b22b-47bbb689f80f | -11.83358 | -46.7731 | 2026-08-29 04:53:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0004c2de-74f4-339a-818a-c95682473869 | -9.26622 | -45.64607 | 2026-08-29 04:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 04cd12ce-c04c-3710-b3ca-32941eff0d43 | -9.66307 | -55.08309 | 2026-08-29 04:53:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64984dec-9115-3567-8d1d-a0b4a0b120da | -11.26332 | -54.01689 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c25c533e-c600-36ac-934d-128a9a95a986 | -7.29597 | -49.96256 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cdf2355-4801-36cb-8e4b-8ba75080565f | -6.27288 | -53.14368 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6a28ce9-70c4-3711-9315-c591500669f6 | -11.27811 | -54.01173 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58d508bf-26e6-3af8-8670-5193e74163ba | -12.76449 | -44.26553 | 2026-08-29 04:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d31041a-8f6e-31f8-85dc-e6afc5513f08 | -7.55782 | -61.31034 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1e974492-321f-39b5-b704-40c467f737a7 | -11.03916 | -57.23408 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da2fe4df-777d-31a8-88e9-9ce755169df8 | -11.21466 | -53.98976 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 783e028d-b81b-3cc8-a93e-83e94c0670ce | -12.24236 | -50.53588 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06ca530c-e2b3-3ce6-aa34-d1d70b3ef8f3 | -7.94662 | -52.44544 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d1132fd-8378-331d-8195-e4d13b89edda | -11.36525 | -45.14145 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 22e8be4f-7196-3746-97a3-11a644786e16 | -11.48687 | -45.1047 | 2026-08-29 04:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f0779049-d4ba-353c-a4ec-ca520df69045 | -15.56941 | -56.28008 | 2026-08-29 04:53:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62853a2f-a420-358b-8fcd-b7f121b9d4aa | -12.78137 | -46.45743 | 2026-08-29 04:53:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2791f171-cb3f-31ba-9920-cb28dea43b67 | -9.17922 | -59.6363 | 2026-08-29 04:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12e6c342-453e-379d-9a04-16403722ba93 | -7.28418 | -49.97168 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f157034-7280-3467-a994-390cb2209594 | -7.35836 | -55.1698 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98f178dc-b64d-38bb-9b05-0defacf520c7 | -8.99261 | -50.79287 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16416ab7-8274-3c78-aa6c-5e904d6455da | -9.93846 | -60.43219 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb6e3b6f-aecd-3858-b490-f5a354822c87 | -9.96432 | -53.93415 | 2026-08-29 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 63bc208a-99a1-3dec-868a-9a8728b41a4c | -8.94922 | -62.40485 | 2026-08-29 04:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d61418d2-610a-3cf5-9a23-85930a5e1bb8 | -6.8412 | -59.93774 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cc28ae3-ef22-35f4-919b-11a46eb51801 | -11.03269 | -57.24738 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4fafbee9-2924-3965-8f42-9f5fa891ff13 | -7.27563 | -49.84822 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74b3d8ae-9121-360f-8a16-0a40b52ccb0b | -7.27507 | -49.85184 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c74df5e-412a-3c7e-89db-e2febce7fb96 | -11.48211 | -46.94907 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a7d4220-5d09-3148-9662-90b8c3ef13e8 | -18.78216 | -45.59447 | 2026-08-29 04:53:00 | NOAA-20 | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42d9c3fb-8b98-3f39-be0f-34432d525f5b | -17.28475 | -46.02486 | 2026-08-29 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e29f71e-982f-328b-ae9e-a5e4236f7fbe | -7.27855 | -45.85979 | 2026-08-29 04:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9103ebfa-5222-34ce-b710-4c92b2b8a7dd | -6.57369 | -56.5478 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9face2e4-05fd-3656-b100-da791819907e | -7.17434 | -43.17723 | 2026-08-29 04:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8bdb92c5-e9a9-3694-9916-534a60a2f629 | -17.82648 | -50.95256 | 2026-08-29 04:53:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 363cf644-7f2b-3c2e-b54c-c20690c6a79e | -8.01943 | -51.81989 | 2026-08-29 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d30d60e7-1d29-3673-8df0-4188aabe01f5 | -11.24029 | -45.07445 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea97f3d0-2a4f-365f-a624-9fc064b3c0fd | -5.89287 | -51.68966 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5156ea4f-d99c-34c7-8f0e-3675fabec950 | -8.50577 | -55.34373 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78b1cd45-4418-3e61-86af-884ee50642f7 | -11.03382 | -57.21792 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7819cd26-4694-3b5f-8a31-d0185636a00a | -6.75403 | -55.67807 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 28c1499d-b97e-36fe-bc07-b9f33ae9d78c | -11.22544 | -53.98777 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7836692-cec1-3e0a-bf39-dd9225134948 | -8.9589 | -62.3853 | 2026-08-29 04:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a45b9cc2-ed7f-359d-88ea-cc0f139f1aa4 | -19.26925 | -49.51368 | 2026-08-29 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c91f828-f761-3b43-b324-54d62852605a | -7.6092 | -47.2875 | 2026-08-29 04:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 43c19708-311a-312b-b661-9dace021b9df | -12.43181 | -43.41225 | 2026-08-29 04:53:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f48b3cf3-c280-3ada-828f-b4317d2da0bf | -6.8442 | -59.95082 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66b522a3-c473-348e-9025-0b2abdaa64bd | -6.53616 | -55.24286 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec966b2a-4248-3851-b9c3-5868a28eae9c | -10.88713 | -50.4976 | 2026-08-29 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc5b2e5f-9b6e-3d62-ab85-04d777f9042e | -7.58546 | -61.3424 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4eef5f43-fcc9-32f0-9a99-64c790c20f9d | -6.72522 | -60.014 | 2026-08-29 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf217472-aca1-3237-8169-499a0ec8e135 | -6.15573 | -57.80123 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b8569de-5029-3704-896e-f9fd035d302f | -12.19869 | -50.54885 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e7baa41-31ea-3ac7-8479-8ca8fec4ec54 | -11.7138 | -54.53797 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f70f3cfc-1faf-3b6a-87bc-77eb2c78565b | -11.02849 | -49.68317 | 2026-08-29 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 383b4817-61e4-3c76-8846-dfc920d4a4a2 | -11.48624 | -46.94963 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46b3b4ac-5a85-36a6-ac55-5e3a601b39a6 | -10.40605 | -61.20112 | 2026-08-29 04:53:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08b21a46-ce7b-3ef3-883f-bd4e03d16009 | -8.94406 | -50.18037 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4f17df19-f410-3bb0-8ac8-e0dc0b7c190e | -6.75105 | -58.73042 | 2026-08-29 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3aecbd8-04e8-3df2-9422-3a4660088030 | -9.91737 | -60.43396 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e044cb5-5cad-316b-a911-8dffac3a8b78 | -5.99177 | -57.68179 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5debf38c-abce-35a6-ad26-8f299d9e7fad | -10.54518 | -50.46886 | 2026-08-29 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f15b475-741f-3256-90c8-52796b2a5d2f | -11.36788 | -45.13638 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 491f24e1-7066-36b9-9c6f-7704742078e7 | -11.19237 | -55.09262 | 2026-08-29 04:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7647939-a928-386a-91bb-f645de807b38 | -7.29032 | -49.95443 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc1d7146-1889-33aa-87fb-bae09fb6bda5 | -10.75273 | -54.04719 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 317c3507-bfaf-3de5-b24e-386d4fbab0de | -8.48823 | -50.41063 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c03d076-8973-317c-8f64-de6f622933b2 | -8.59984 | -54.77238 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcfd828e-76f9-3656-bd40-006580b3229c | -11.60307 | -46.72731 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f66287dd-434b-3ddc-827f-d2c1ffead8ba | -9.92293 | -60.43197 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70aaea63-18d4-34d6-8ce4-e8fc461deb79 | -9.86508 | -60.29865 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eba997d1-6704-36e2-810b-7a83fbf223e0 | -11.02871 | -57.24666 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a28d8cc-9b40-31d4-880c-117d5da04b47 | -7.96166 | -52.43689 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5ea32c6-d4e5-3506-a750-f65a500dae19 | -7.29093 | -49.97273 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51de92d4-0362-3259-a25c-8e34b058c656 | -9.86692 | -65.03748 | 2026-08-29 04:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab1f6d58-d393-34aa-99ad-2765e80e9c78 | -11.1959 | -55.09322 | 2026-08-29 04:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a42f5505-30c8-3fe4-9301-62c581248790 | -6.83963 | -59.94675 | 2026-08-29 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5aa04604-53fd-375c-aa28-00442417ccd9 | -8.62647 | -54.6912 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3ea5835-8f4f-3549-b613-f80af111442b | -10.5564 | -59.61846 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b645038e-9f00-36e6-a96f-a679c8f90c47 | -11.60726 | -46.72796 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0773a4fe-428d-3f9e-8c74-fbd256b1b9ea | -7.8571 | -56.68451 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c305f8fb-9747-34a2-aa0f-22f5e84be808 | -6.86459 | -59.03521 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README51.md)
