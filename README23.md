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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1dbdedc-8e3f-34a2-b136-122fbc64c8e8 | -10.78514 | -45.93764 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 43b12334-04c4-3f5b-8161-400c98c28ff1 | -13.73335 | -48.97715 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4a8330f-46f7-337e-9a28-d3da78773a9d | -14.5822 | -48.85291 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7d342b3d-5fb6-3073-9fd3-9591d352761a | -8.83657 | -62.4791 | 2026-09-11 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f5816b01-3fe4-3e14-9ccc-e5fcf169e3a7 | -14.6017 | -48.86755 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c2309af-04d4-3f03-b62c-9d8453057983 | -13.29725 | -61.82362 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a19a3f93-38e3-3d57-8197-791380e9e164 | -13.48766 | -48.55642 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 87690434-39d3-3133-bf13-3e9a5421adcb | -10.54297 | -51.35333 | 2026-09-11 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4884faee-893e-37f3-b0e8-e83b0752fbeb | -8.63194 | -66.50459 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2be0023c-b725-335b-bff7-018e87bf4c37 | -8.46397 | -64.05023 | 2026-09-11 04:53:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e971179-1a91-3255-ac2e-709f396b6493 | -10.53525 | -54.38216 | 2026-09-11 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a25474ad-6086-3773-b9c4-50b040bbfc0d | -11.80666 | -60.45656 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2ebe7b69-1d1f-3869-9c71-a6016b92e83a | -14.6037 | -48.8523 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43b1ef02-24fa-346a-acb0-73c95486931a | -13.50776 | -44.06995 | 2026-09-11 04:53:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8bd4da83-4483-3111-9750-ad986012decb | -10.53951 | -51.35272 | 2026-09-11 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83217cd9-8bf8-3dac-97de-b03662a8f6b8 | -14.78774 | -48.08478 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d100964-eb01-3b7e-8881-161ce50bda83 | -9.30093 | -65.8899 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09a39c94-99a8-3346-8a02-c2d50454cefe | -9.75612 | -65.0331 | 2026-09-11 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de8ad458-91f7-3378-a557-412389388dd1 | -12.01335 | -61.84615 | 2026-09-11 04:53:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cb9b0a5f-563f-3ca1-8e05-def7a3280eb9 | -11.81027 | -60.46164 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cb4f52dd-ba1c-3b64-8fc0-c3459d8f7392 | -13.21683 | -61.64467 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6ae305ed-34ab-3e1f-b17b-584152932da8 | -9.22042 | -65.57699 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f717e9b9-a40b-34d7-b296-bb276d0f72b9 | -12.16005 | -64.13721 | 2026-09-11 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9cc60e94-d546-32fb-b631-26ec1580aa25 | -13.77194 | -43.64454 | 2026-09-11 04:53:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e07fc76-f017-30a3-836d-294a32c5d3dc | -13.22247 | -61.69181 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0aac18c-24a9-3e00-bf45-2a7c2bf22413 | -13.35371 | -61.67443 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 743c2ff8-fe86-30dd-9ce2-f01fb650e772 | -12.15932 | -64.14101 | 2026-09-11 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3db206a3-b650-30fb-8c47-0ff4b702766f | -9.22778 | -65.57306 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26795f10-0580-3aaf-9124-85eaed7af57a | -9.75511 | -64.94033 | 2026-09-11 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 420a035a-6bde-3a25-bafd-f8b5c4188938 | -11.29681 | -54.03812 | 2026-09-11 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8757fa62-ae07-3670-b080-c4f10c51128b | -13.34908 | -61.67355 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 73844efa-e2ef-3adf-bef1-7bb5c1426dd2 | -10.46743 | -48.65621 | 2026-09-11 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e87b074-7b72-3535-865f-82e799b66c6f | -9.04261 | -65.41805 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0399cd32-7a9a-31bb-9506-1717b0b5107a | -11.24289 | -54.14426 | 2026-09-11 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4606a24-c03c-3788-b623-1d366feea09b | -11.94841 | -49.74726 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a44fa55d-5aa4-337c-ab82-e404c420be4f | -11.40605 | -62.03233 | 2026-09-11 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67337a6a-2b5f-30a4-97d7-bc14ec19205d | -19.37367 | -44.79952 | 2026-09-11 04:55:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5538ced-b664-3b8a-b73d-43af22b054c4 | -20.49479 | -57.46545 | 2026-09-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.7 |
| b9bb14d2-8287-39ee-8a51-87b674a9c0a2 | -18.47517 | -51.74923 | 2026-09-11 04:55:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 422e6615-a3a6-3e9d-8ded-b551ca8c6a36 | -18.47673 | -51.75134 | 2026-09-11 04:55:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9504aa66-3cd2-3a9e-9576-66f05733e143 | -22.2754 | -55.84367 | 2026-09-11 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 714d89f2-97bc-39af-9c0e-6e5e5cebae7f | -20.48869 | -57.46042 | 2026-09-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b2508b01-4e7d-3d50-bdaa-609747930140 | -22.26933 | -55.83875 | 2026-09-11 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2528baaa-d6a2-33b3-9212-56a965f381ad | -20.4908 | -57.46863 | 2026-09-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5f12b6cf-4ba0-3129-b302-44eb89fb384f | -18.47889 | -51.74978 | 2026-09-11 04:55:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d1480dc-dcd4-3988-8eef-0a7596b10b74 | -21.69117 | -56.52335 | 2026-09-11 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d5a664a-2c7d-3a75-92ad-c2cbf3b5a8a4 | -20.49143 | -57.46483 | 2026-09-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 77861a9e-29b4-3f55-a912-1afb048bbc04 | -18.47827 | -51.75443 | 2026-09-11 04:55:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 814e62c6-ee40-3708-bff9-a77b2569cc0e | -19.01238 | -49.4814 | 2026-09-11 04:55:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 777375c5-99a0-36e0-9dd5-3d04aa944ff9 | -16.75865 | -51.87125 | 2026-09-11 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9e39680-07ad-39bd-a709-9ed63ae5e966 | -20.48807 | -57.46422 | 2026-09-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b2f277f4-3146-313a-9b22-218129d1a933 | -22.26155 | -55.84507 | 2026-09-11 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30f3e75b-69b9-3521-ac38-9404e0a062f0 | -20.49815 | -57.46608 | 2026-09-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.7 |
| e1128aff-1923-3e27-bb9b-ba4182c4c32f | -18.47737 | -51.74672 | 2026-09-11 04:55:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5df7b568-b101-340a-b62f-54040e8ba7cb | -18.47302 | -51.7508 | 2026-09-11 04:55:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fad2ff13-b7b5-3ab5-aba9-4257ebd8b1ff | -22.27321 | -55.83559 | 2026-09-11 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8af07052-1c47-3657-b16c-e83a42edfe9f | -22.26989 | -55.835 | 2026-09-11 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac38ec6b-d841-3f36-a0be-3620105085e4 | -18.4795 | -51.74514 | 2026-09-11 04:55:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10c8f3d7-d31c-3a74-843e-dfaf463b703d | -22.26543 | -55.84191 | 2026-09-11 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 326dad99-7964-3270-863b-2a255e019408 | -18.48044 | -51.75193 | 2026-09-11 04:55:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 818d7b63-d81e-323b-bc0e-649991e02f5f | -20.4847 | -57.4636 | 2026-09-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cb59f7c1-5075-36e9-90b7-316874a5f94b | -22.27872 | -55.84425 | 2026-09-11 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 468f5634-6560-3eb6-bed4-b160cce3335c | -22.27094 | -55.85057 | 2026-09-11 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d0a5702-5988-389b-861a-1a9abea9650b | -18.48108 | -51.74731 | 2026-09-11 04:55:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d120810-1e10-3536-9532-79730bdc0840 | -22.266 | -55.83816 | 2026-09-11 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c56698a-5dbf-3e38-b6c9-10972d31aae1 | -20.46517 | -57.4561 | 2026-09-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 05e2a96b-99a8-3ecb-9326-09244a97dc98 | -22.26487 | -55.84565 | 2026-09-11 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8101348f-2662-37d0-bef3-91bfdc9e2bd0 | -22.26211 | -55.84132 | 2026-09-11 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa77d5b0-ec8e-3202-9b8f-baf58ae56fb6 | -30.64831 | -53.60065 | 2026-09-11 04:57:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 7fd6f569-a2aa-388a-a957-677d6917bf1f | -30.65284 | -53.59563 | 2026-09-11 04:57:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 156998d5-fa66-325c-a66c-985cb25e6912 | -9.1799 | -68.2194 | 2026-09-11 05:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| efd39c0c-a0db-305f-9f1e-87f8fd3f67be | 2.51011 | -50.84939 | 2026-09-11 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a4cc2bd-4e73-3d10-9401-5ae3f8181602 | 2.51447 | -50.84872 | 2026-09-11 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccb863ad-403e-39b4-9b68-abf18f9d40dd | 0.97038 | -51.12934 | 2026-09-11 05:25:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53dc02c3-d574-373b-9eda-b672608c81e6 | 1.29279 | -50.67517 | 2026-09-11 05:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c69374d-8de8-38c0-a284-e8ca036fb9b9 | -0.43797 | -52.07564 | 2026-09-11 05:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0b34f89-1b5e-3f7a-b44b-f514e9e20258 | 1.28451 | -50.68109 | 2026-09-11 05:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd41663f-61e8-3f54-b395-e200ca54bba2 | 0.97393 | -51.12628 | 2026-09-11 05:25:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88e5bf69-8625-3d49-8494-dee1c3eca47e | 1.28002 | -50.68183 | 2026-09-11 05:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a68f88d3-08cd-3f71-a312-dd662aa2e27e | 1.28829 | -50.6759 | 2026-09-11 05:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 855bbb2c-0783-36f9-a1ca-25da254aeb43 | 1.32195 | -60.71112 | 2026-09-11 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae229953-1a0b-35ab-ae95-d3a460c9d048 | 2.66574 | -50.86459 | 2026-09-11 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 08098fc2-6905-3ee9-b553-856a49a7c5e5 | 1.2529 | -50.71371 | 2026-09-11 05:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8e56965-e30b-3b13-9ec5-af5cefcdd49b | 4.75711 | -60.42999 | 2026-09-11 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9518433b-a224-3f31-b3dc-4f54895427dd | 2.6614 | -50.86531 | 2026-09-11 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7cbc487f-af13-33cd-ac0d-9087c1866d6d | 0.98202 | -51.1207 | 2026-09-11 05:25:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2235bc31-3f65-39c2-a350-b9f87074ca13 | 2.50943 | -50.84519 | 2026-09-11 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d327b35-6ab6-3e74-8c8b-f5b86ada237b | 1.28073 | -50.6863 | 2026-09-11 05:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8ff25f3-9c0a-396e-9362-0504e5cdfbcc | 4.48982 | -60.85491 | 2026-09-11 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57ce1288-3769-34c1-b37d-a3b4a85a17a3 | 2.49252 | -50.98769 | 2026-09-11 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ba2fc38-d093-324e-98db-3dd7620be82e | 0.97024 | -51.13116 | 2026-09-11 05:25:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a16cb684-bafc-371b-b1f9-ad511f66cb72 | 0.97462 | -51.13046 | 2026-09-11 05:25:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b03108f9-bda8-305b-9562-ff86e5aac49b | 4.18091 | -60.29217 | 2026-09-11 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 387bf180-7db7-3868-8c69-186f58bd1013 | 2.5138 | -50.84454 | 2026-09-11 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5e132c0-a8c3-3278-8979-ce2dae03ebe8 | 1.28901 | -50.68037 | 2026-09-11 05:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51a55f19-5ed8-3213-b104-f110d21316f3 | 4.75921 | -60.44383 | 2026-09-11 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39159b1c-c74c-30ee-934b-257f48e56e3c | -5.9743 | -57.77187 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9191bbdc-d330-358d-9376-6b85e5a9c728 | -3.06467 | -49.5189 | 2026-09-11 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15023bd4-39b6-336f-aab8-12a63c9af3ac | -4.53429 | -54.95916 | 2026-09-11 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f0bec3b8-17b7-3b63-9784-e0dd0e579f44 | -2.89315 | -57.1862 | 2026-09-11 05:27:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
