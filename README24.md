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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7864d5de-e7ed-3c91-9523-d880fc84e08a | -9.92446 | -59.90262 | 2025-07-10 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bcf78a9-f9d6-3bd5-97c4-51d0e6d1902e | -10.29609 | -60.54579 | 2025-07-10 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a50a5588-f3cc-3559-bf72-68c845087825 | -10.5776 | -49.13205 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 76ebc8f9-03ee-3245-8085-78bface00b57 | -7.89258 | -61.47717 | 2025-07-10 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e81055e3-0a2c-3661-b426-49639b27f958 | -13.16307 | -47.27388 | 2025-07-10 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 618aa428-6c5c-31a7-bb5b-0be132517c7b | -7.1758 | -59.83661 | 2025-07-10 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af46876a-a36f-3be0-a2e4-6c4a0391e118 | -9.70573 | -56.09153 | 2025-07-10 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 82460f43-d002-301b-ace6-5c8c0d304b01 | -11.33051 | -51.44525 | 2025-07-10 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd2a19a4-8e29-3a14-8de4-b29c0f1c9af4 | -7.46453 | -49.40203 | 2025-07-10 05:18:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 843b6e54-68f2-3085-bef8-fdf288e514e2 | -10.6618 | -49.45762 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b69ab135-da34-3cc6-a3ab-066c5686b9a2 | -13.37015 | -47.89762 | 2025-07-10 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5ad55dcb-aa6c-3880-aa77-2be5a874916a | -11.32533 | -51.44455 | 2025-07-10 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 469c3445-d518-3ae0-ae3d-c1bbdc598ad6 | -13.15554 | -47.27935 | 2025-07-10 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 162fc3f0-24c7-3b2a-860f-a987a2c167ee | -10.22814 | -56.7686 | 2025-07-10 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87ddf124-38eb-3c2d-a7fa-beb518d5fe3b | -12.5726 | -48.88453 | 2025-07-10 05:18:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 832426d6-1a24-3af8-be9c-9c21dbb570c7 | -10.65493 | -49.4651 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 44653627-f232-3625-b668-06603db282b2 | -10.57652 | -49.14094 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| a15d9e2f-8797-31df-8898-15877048207b | -7.46505 | -49.39817 | 2025-07-10 05:18:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 722a9562-7ad5-3238-9f3c-80a92aa1d1e4 | -9.54064 | -49.57938 | 2025-07-10 05:18:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e4d6834-b83b-3f37-9e8d-12ce395ff1db | -10.23175 | -56.76912 | 2025-07-10 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04c7d3c9-245d-34c6-8836-7f733b334a87 | -11.33127 | -55.21821 | 2025-07-10 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 194a2901-d3a6-3c2c-bbe0-0ee8e7f5824b | -10.57488 | -49.15433 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| b9a2181c-e2b9-3b18-a4f9-e1c6cce9a1ac | -8.85793 | -47.94885 | 2025-07-10 05:18:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 653fb646-670f-38e1-be5f-7db1f143239e | -8.86177 | -47.94726 | 2025-07-10 05:18:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6de87cd9-da22-32ac-928d-aeb02b98e04f | -9.21894 | -48.59917 | 2025-07-10 05:18:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ea6cb3f-16fc-3fb3-bdb8-dc9a7a7a888b | -9.21167 | -48.59746 | 2025-07-10 05:18:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 552486f2-f11f-3bc3-8f11-c4bf3c10e848 | -10.35005 | -57.5042 | 2025-07-10 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 351a77dd-e6f5-3182-9677-9b699cb64981 | -10.58136 | -49.15089 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63802acc-942b-36d0-907d-b5f424846a60 | -11.3708 | -48.70991 | 2025-07-10 05:18:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3a356944-4560-3c22-b464-c49ceb169903 | -10.87703 | -54.04684 | 2025-07-10 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a463461e-a376-3912-8c2f-bf473534b488 | -13.39007 | -47.87606 | 2025-07-10 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f7dbb20e-0c95-30a6-b74c-29c0a577e49e | -8.96657 | -49.85774 | 2025-07-10 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7291f87e-d5f9-378e-b5e1-73d93636c41c | -10.9021 | -46.73456 | 2025-07-10 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2465332d-0361-36b9-bd96-23d4822e2d53 | -9.24763 | -58.76221 | 2025-07-10 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7984a4c-c20e-3d5d-b452-c4d4204e7981 | -10.65544 | -49.46092 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 147d93eb-94f0-3d2f-ba30-3502e4dd9952 | -6.62837 | -56.27782 | 2025-07-10 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 705f9119-50af-338e-aee8-e182fc90df2c | -13.15567 | -47.27511 | 2025-07-10 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13bd6ce1-e711-327c-80ea-2da35565c326 | -9.46097 | -62.20488 | 2025-07-10 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b8ecc7c-684b-33e9-94cb-f61b61f066ac | -10.66025 | -49.4701 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7de55d51-c135-3289-8e51-42966d77350e | -9.73083 | -61.40487 | 2025-07-10 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd42b034-7f47-38b2-9dfa-46d475d98d95 | -13.37754 | -47.89153 | 2025-07-10 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0112a7ba-74e6-31b9-9e33-8ddcd2f63b5d | -11.35207 | -55.40504 | 2025-07-10 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a4ad469-ce3f-3d06-ad89-aab886d37479 | -9.92947 | -59.93553 | 2025-07-10 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e99eed4b-0b2a-3fad-88e2-a1658a4b07f2 | -8.69998 | -64.11893 | 2025-07-10 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c62626c5-7d9b-39f1-b6c8-b3beacf86d91 | -6.26696 | -57.40584 | 2025-07-10 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bdd1a2e-c506-3fb3-a09e-7935e4f0e7c0 | -6.62811 | -56.2834 | 2025-07-10 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75229bb0-f332-3e3a-b139-ec149bf6ebff | -10.8908 | -56.45514 | 2025-07-10 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d279f071-4e55-3283-8b07-e1a66caad1b5 | -13.37091 | -47.89048 | 2025-07-10 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0b19fb40-bf86-3034-88ca-f02800b41c22 | -9.48354 | -62.55575 | 2025-07-10 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d08fa94-df38-30c8-b56a-b171414168ed | -8.69915 | -64.12383 | 2025-07-10 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a4bd0d4-bf97-387d-ace8-26bf08bc5dc9 | -9.54014 | -49.58336 | 2025-07-10 05:18:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f415b70-bca5-31f9-a952-b6d6e1e71460 | -11.87426 | -58.71567 | 2025-07-10 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dad1629a-8282-3242-bdb0-b03012d35214 | -8.33869 | -55.1008 | 2025-07-10 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb12c74f-ba4c-3d80-a906-d04b49d83e11 | -9.88236 | -63.11145 | 2025-07-10 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95f8e805-ef9c-3000-a174-e3a034383c30 | -10.66661 | -49.46676 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 254126ab-9455-3d3b-8e5e-75d2a64d33c5 | -8.86115 | -47.9523 | 2025-07-10 05:18:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d302bf18-4e49-3dc4-b4bc-27916457568d | -12.99446 | -47.82689 | 2025-07-10 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e10ad0c9-d5c1-3e8c-961e-ac29ede94b63 | -10.56948 | -49.14899 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 274756ec-fc10-3076-a430-16d62e290462 | -13.39237 | -47.87902 | 2025-07-10 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 594ade0f-315c-32fa-87a0-31ee4e19cf62 | -9.21288 | -48.59826 | 2025-07-10 05:18:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb2092f0-102d-3145-93fa-ed58038ffbc1 | -11.87371 | -58.71936 | 2025-07-10 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59e3d1b1-fe64-3b55-a604-9f4612062d2d | -11.83152 | -48.21879 | 2025-07-10 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cb5ff085-353c-3364-a5ab-8aee9f290178 | -10.66764 | -49.45844 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5b61c8cd-fa0b-310d-9421-635d2d677fd2 | -11.32777 | -55.2141 | 2025-07-10 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fa4bcdb-5d68-332c-8870-205efce68238 | -13.16199 | -47.28122 | 2025-07-10 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e7c8b9f0-93d2-34fe-bdb6-28705fbba028 | -13.28827 | -49.15833 | 2025-07-10 05:18:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d03b9bf5-44e2-30b9-9e0c-27a5f88c8551 | -11.33296 | -55.21769 | 2025-07-10 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cc1aa4a-f626-3e9a-8159-2857aaf1eb23 | -10.66713 | -49.46259 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 736761f8-9235-32c5-9cb7-4b5bb44d2035 | -13.16249 | -47.27953 | 2025-07-10 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1bd6ffe0-fe18-3d16-a843-5baa675f7732 | -13.15503 | -47.28111 | 2025-07-10 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c503d25-0b64-3aeb-9531-3de9acd79354 | -10.89519 | -46.73356 | 2025-07-10 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dda2df9a-5dfb-3a27-9cd0-4dec127a7257 | -9.65941 | -49.89214 | 2025-07-10 05:18:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1b2448b-f7b7-3f2c-a9e7-c802d469efaa | -12.57766 | -48.88314 | 2025-07-10 05:18:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c2f2712-066a-39aa-900e-6eb472240a2c | -6.62517 | -56.27881 | 2025-07-10 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d349c607-0d57-3429-98d0-006c5d81b8b1 | -12.47262 | -46.91222 | 2025-07-10 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac39d1c8-7e11-378e-ad5c-df3b2e947002 | -12.56436 | -52.21955 | 2025-07-10 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fbf8ddc-6dfc-31ad-a030-be9c67403544 | -10.57708 | -49.13637 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7507f9f2-97ff-371b-bd8b-6d6568e4a41e | -11.87959 | -46.76484 | 2025-07-10 05:18:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce599183-fd5b-3fd7-853c-1f47963ae50a | -10.66128 | -49.46182 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 505933af-1c35-32ab-9c03-5e2a58dbe92f | -6.27035 | -57.40637 | 2025-07-10 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ed6b633-8219-369e-95d7-beeea912f53c | -7.89956 | -61.52073 | 2025-07-10 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 587b47cd-7461-3cde-a876-3c5480fe6bd2 | -10.57058 | -49.13991 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 9bef3776-b3ba-3e68-9c6e-6ca2312f14be | -7.70545 | -45.77357 | 2025-07-10 05:18:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f4e4edc2-7143-3a4a-9ee3-979d7159ca7c | -6.80293 | -59.04662 | 2025-07-10 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cdd67980-25ab-3312-aa14-88dd33a4ebba | -13.38492 | -47.88551 | 2025-07-10 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a87ee7e-380f-3ee6-905a-f83b655e56b4 | -11.37136 | -48.70514 | 2025-07-10 05:18:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d34ca78-8534-307a-bd27-94cdcccfbe5d | -10.57595 | -49.14559 | 2025-07-10 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 47953d2e-4d50-3e85-bf87-8fc67048714f | -8.8573 | -47.9538 | 2025-07-10 05:18:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 69720326-ecca-3f15-b896-a00d130ca027 | -9.51158 | -55.96069 | 2025-07-10 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 626844f7-28b8-377a-8df5-c1d98f43b821 | -11.80872 | -58.85247 | 2025-07-10 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 393b3787-5119-34c9-9cd7-61dec6c3ce19 | -9.33669 | -58.84555 | 2025-07-10 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41c4d532-9a01-3577-ac6a-04acf32147dd | -13.36959 | -47.90278 | 2025-07-10 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 150df7c6-079b-3ea3-b844-0a4067ea9e10 | -9.21772 | -48.59836 | 2025-07-10 05:18:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6e9239d-5bb0-313e-b0d4-3e0401112122 | -8.88984 | -47.33553 | 2025-07-10 05:18:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2030ea89-8073-3a58-ac8f-b566a7daf414 | -13.37836 | -47.88384 | 2025-07-10 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 339ee0a1-61ca-3d93-b9aa-c346a926e68d | -6.63192 | -56.2784 | 2025-07-10 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38e619ca-4197-30ec-b6fa-589ef2fcced4 | -9.02618 | -61.22737 | 2025-07-10 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39498868-7611-3e94-b4a9-ba936f85f85d | -6.62579 | -56.27476 | 2025-07-10 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc2e69f0-7fef-368a-8304-1ed2e9405c2b | -10.86374 | -54.30583 | 2025-07-10 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 084c4ac7-335c-367c-8cb5-cc0510377e77 | -13.38577 | -47.87761 | 2025-07-10 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README25.md)
