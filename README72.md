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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4e5a5ef-b7c4-35ee-b385-24cedaf670eb | -10.79159 | -50.98345 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0935b672-fcf4-311f-b270-fd0cdfbb0dcd | -9.41268 | -60.42823 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e86fe23-6a71-37b4-a630-3d7272b60e4b | -9.41823 | -60.41475 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1a26340-4e2e-328f-aba7-91f456483e63 | -9.10242 | -60.92171 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 462d4a88-65df-3ce3-89c0-bb76ae9e12fc | -9.41547 | -60.4107 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e76d1fa-88ab-33ad-80b3-a0fb39d1f3bb | -9.15087 | -59.55278 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18513f58-9873-30f8-8568-5e59d537eede | -11.1359 | -49.03958 | 2026-08-22 05:25:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2e90d2e-09a7-34f9-a9e7-fa921727e7bf | -9.17102 | -57.00573 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c686f373-a530-3e09-b6aa-b8f2ccfae920 | -7.8663 | -63.76637 | 2026-08-22 05:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd88398e-3562-3ca2-96f9-99ee031c8cd0 | -9.39637 | -60.55167 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 123c7f1b-21ad-3d21-b4ac-2212fda389d0 | -9.24527 | -60.79544 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ee2b2e2-c3cb-324b-88aa-5c4c570b4f54 | -10.52861 | -50.77607 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8e49c8e-bae3-3d7b-ad53-178f97aba3b6 | -9.44295 | -51.61595 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d829ea85-a315-3437-b516-aa58818bb288 | -9.43651 | -51.62614 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb3b5188-f43e-374a-8761-5884a7a34a61 | -9.16016 | -59.47212 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88d1a06f-e881-383b-a9df-ee652be8a615 | -9.21552 | -59.76653 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1710c4bb-9014-3cc7-89a6-97d2aea3c3cc | -10.6789 | -50.30009 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82d25957-f285-3abc-82c8-9c4e6b02f695 | -9.16457 | -59.46567 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1cea6545-38cb-339f-ac80-5b819b6c1ec3 | -9.12291 | -61.59729 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98acc24e-dfcc-3216-95b9-2c203cf43571 | -11.10533 | -49.89013 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 661b5810-ed4d-34d6-bebf-6e228d311e8e | -9.21166 | -59.76948 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73286f57-2a0f-3545-a886-32f513940032 | -9.40828 | -60.41313 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a90dfb29-45f3-3c33-8f07-c0ae88e40fbc | -9.17456 | -57.00629 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 327e4c25-7b21-3afe-9142-6643296d71c7 | -9.40496 | -60.4126 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7719033a-3c92-3cc7-b0db-5105259b8f9b | -9.40246 | -60.55627 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00eb3920-e427-3d76-9a81-3a6271bc703f | -15.20206 | -52.78028 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c2b6661-dcaa-3ca1-81f6-0712e1d19da5 | -9.2078 | -59.77243 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23fe6e6f-94da-3736-97f5-990cb7f094a4 | -9.41603 | -60.4072 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79fa504c-6ad1-318d-9da3-71e0943b75c3 | -11.59819 | -46.56047 | 2026-08-22 05:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 290f7c8b-8a1c-36c0-a9d1-5b36834bb306 | -9.43508 | -51.63711 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c2c82d9-b6af-367c-bdd8-b17aa1584577 | -7.90532 | -61.72993 | 2026-08-22 05:25:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c778ab1-e6ae-3d76-8238-f99ee1770752 | -9.1201 | -61.593 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ea8658c-4674-397f-a1b5-8107b5d6e242 | -10.51718 | -50.8233 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9304c34f-0edf-385b-bfdc-19135ddbd67a | -9.17517 | -57.00229 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b00fc7e5-ffc0-3f98-8310-b885f7e8cf3b | -10.81218 | -50.98018 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4d6e508c-4f14-3129-ba4a-68148f912a28 | -15.33693 | -52.92712 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a12106b4-cf4b-3e44-a999-368b28bf6c59 | -9.12632 | -61.59785 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8d6a071-6451-3e19-8452-37df587d9fe1 | -10.51824 | -50.77145 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dac9124b-2887-3496-a5b1-8d91c460d03b | -9.40772 | -60.41664 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d98622e-8341-32d9-b851-9acfd4ea4de6 | -10.90384 | -50.24109 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63515dcd-0f03-3e8d-9d57-61d0051daf41 | -9.05819 | -60.43534 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 162ac942-ea46-3011-b6ac-6158a3836f52 | -9.17667 | -57.064 | 2026-08-22 05:25:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a1fd325-59e6-308c-b295-90d8a9bdf1a5 | -10.90034 | -50.23667 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e2f0d9b-fa40-31ed-ba50-362e8138f217 | -8.39779 | -62.68778 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 600d5587-1614-31a2-a62b-3bb2325dcb2c | -9.17174 | -59.46324 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8851914e-39e8-334c-8ae4-8df7d10d0121 | -9.40436 | -60.43769 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c371686-6ea7-3286-b0ab-e517d565f00a | -9.525 | -51.65002 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6cb4dd27-60c6-3b35-a0c0-5a64e87ac889 | -9.21997 | -59.78152 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18fba712-7069-30a9-b4d1-34554ea9ca6b | -9.05042 | -60.44127 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8065e66a-7415-3f71-aa86-a5f7371a1d51 | -10.89935 | -50.24426 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 754f6d01-8bb4-31cd-904c-a32732176e98 | -9.40768 | -60.43822 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d6e3f51-d0b3-374e-a968-edcb33c61100 | -9.17042 | -57.00973 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38ce765b-1823-3fee-ad23-42a568baa821 | -9.17931 | -56.99888 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 349c7bc9-4a74-366f-bbce-91b11285af9a | -16.48952 | -47.9441 | 2026-08-22 05:25:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9284a19d-e9b8-32a7-84a1-c105f53a2452 | -7.86167 | -63.77051 | 2026-08-22 05:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9278fdb3-8f29-3c90-b653-50ae8985a63c | -9.45057 | -51.59676 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d807c42-2266-3c63-8849-047e55a8c74a | -8.4043 | -62.69313 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b76406b-06b4-3026-92ca-78bc4850e12e | -9.17669 | -59.45331 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 496034ad-d846-395e-95bb-7d7ab93add2a | -10.03836 | -59.45832 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c92462af-775c-3a54-9599-336449f16c8a | -9.06871 | -60.43345 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c3d2a2d-f3c0-37b2-964f-e87410ab9d07 | -9.28502 | -60.90395 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08041273-7e8c-3de4-8cef-f9040a0b0cd2 | -9.06927 | -60.42994 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1587473-fde4-3583-baa3-457d1b7e2b5c | -10.77298 | -51.00147 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d942ce8-190c-3192-a0fd-d1859272514b | -14.50583 | -59.82345 | 2026-08-22 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb5be6c1-51f8-34d2-828c-e731c9dda772 | -9.28052 | -60.91053 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd4837ad-6f5d-3699-a82d-86723a42cd91 | -11.34613 | -46.35765 | 2026-08-22 05:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c1f8092-1f7c-3e63-8cfa-065a1a9ab084 | -9.11093 | -60.33963 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c8659eb-1fcc-3b22-9b0f-4aa2601c4620 | -8.40206 | -62.68425 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33bb0508-b47f-3e72-85d6-7c8c12250e29 | -7.67053 | -61.12142 | 2026-08-22 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5aed6deb-cdda-3ed7-8425-4445881c9478 | -11.13438 | -49.04441 | 2026-08-22 05:25:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bc8cebc-f931-3e5a-96be-3add388d822d | -9.41491 | -60.4142 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee78ad48-816c-357a-92d4-2ba5b994a32c | -9.1189 | -61.60046 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95bd86c7-9f31-3138-a8b3-4ce64505b76d | -9.16235 | -59.45817 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a25efcf5-e08b-3b1a-ad87-c2ac6bd2ec61 | -9.06371 | -60.44344 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a7f0f29-4ace-32da-bda0-cb9c7c7c28cb | -9.41187 | -60.56141 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06274a5c-bc64-33e0-ba43-301a9eb3abff | -9.16628 | -57.01317 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 472e77bc-3098-32f9-9d43-53046709a3a4 | -9.21496 | -59.77002 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36b42a32-5937-3065-8692-60e377df0939 | -9.20945 | -59.76199 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9cbf5b1-09b0-3fd3-bb3a-455fc01cf9fd | -17.56136 | -47.88755 | 2026-08-22 05:25:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7521d5c0-e7f9-3da7-b70f-307ffa216a7e | -9.1745 | -59.46725 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 439e9ebe-19f8-3a3d-abf4-48ca036eac31 | -9.39084 | -55.97829 | 2026-08-22 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5767d73-3aab-397e-8c41-fa126c86f3db | -9.21776 | -59.77402 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba740856-07e9-3515-8fa9-a23fd2e5a093 | -8.89404 | -60.54615 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05edd4b5-0d28-34fd-9689-ce5bcaf2e431 | -11.62743 | -46.52626 | 2026-08-22 05:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 936ffc86-31a7-34ec-927a-6a96c2267b91 | -16.48896 | -47.95005 | 2026-08-22 05:25:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 740f6d50-ddce-3328-a310-e2c567d67533 | -8.95057 | -60.57703 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a8aee90-454d-3369-b7c6-e3dbd1279c79 | -9.11425 | -60.34017 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e3f592d-2148-37bf-9938-833401e96e18 | -9.58641 | -60.51005 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 368eb128-4e05-38ab-8396-298e68bddbf4 | -9.42099 | -60.41879 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fe34fef-8414-368d-9b9a-e04f00b2d8a6 | -9.40824 | -60.43471 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdee4ff4-33ac-3bf0-b145-856ae2734236 | -8.40362 | -62.69728 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 716ffe35-8784-3853-9b42-1d04ed0386cf | -7.55225 | -62.29538 | 2026-08-22 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19e1d670-2686-355d-82d5-e301352e99d4 | -9.16511 | -59.46218 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e170f3d5-f5aa-3594-b805-1245ef3d85b9 | -8.95773 | -60.59628 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa1db868-3a5d-3982-a463-8054ab9e396d | -9.17836 | -59.46429 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4f70ed42-af65-3b3b-8bd8-75a945201915 | -9.11609 | -61.59617 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91125198-5347-36a5-873c-f8866e758f12 | -15.20521 | -52.79656 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d50ce87c-f02c-3b0e-98b1-c19564dc5b8a | -8.40003 | -62.69667 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e80ad83d-d288-36ae-a485-0187805e54f2 | -15.62931 | -56.13604 | 2026-08-22 05:25:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 317f58f2-f93c-39f9-8004-c6b98f0dc59c | -9.4116 | -60.41367 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README73.md)
