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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c268128-3812-3bcd-a1cb-fa0dfaa98010 | -10.71494 | -44.50113 | 2026-01-31 04:33:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9b6c3db-4ac0-3b87-96e4-c34051e3b611 | -5.24994 | -37.4983 | 2026-01-31 04:33:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 56269ab5-cde8-3c6c-bcc9-765ee9313028 | -5.34261 | -40.84084 | 2026-01-31 04:33:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 41a67727-fa34-3836-8861-4d8620c9bb02 | -10.2894 | -53.97211 | 2026-01-31 04:33:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e654114b-ee82-335e-b13d-ebec67fd030c | -9.47024 | -40.24408 | 2026-01-31 04:33:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c67247e6-821b-3dd2-8f47-3e7089d6c8ab | -8.72639 | -48.32856 | 2026-01-31 04:33:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 854b12aa-846c-3812-8d93-8ee46a1acb97 | -7.60722 | -45.90036 | 2026-01-31 04:33:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21e40854-d505-377e-822c-2bb33e6163f0 | -3.92885 | -47.25684 | 2026-01-31 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96f029e8-9253-357a-8fdc-b45148f2ed6d | -2.78906 | -52.99906 | 2026-01-31 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 663e8a82-4110-3fed-a651-eeb427f939f1 | -8.56524 | -50.00809 | 2026-01-31 04:33:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe0e2bf5-74e1-3736-bb23-1e45821c396c | -7.06995 | -48.03943 | 2026-01-31 04:33:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd31d6dd-ff28-3824-b61c-9adac45ecd54 | -12.29648 | -57.40137 | 2026-01-31 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8c0d2012-bec1-3b43-8740-dadd7d5cff2f | -11.95276 | -58.74322 | 2026-01-31 04:36:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f4f5331-e2c3-3820-969a-5cd0be1fb48b | -15.02727 | -59.67212 | 2026-01-31 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 304c3e64-dce4-319e-a7d3-c97091322c36 | -12.30273 | -57.36836 | 2026-01-31 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39f399e9-ec98-3398-9f1a-606340360a7b | -12.29684 | -57.37293 | 2026-01-31 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc4c5c8d-f960-3487-ae22-27ffce43449f | -15.02656 | -59.67564 | 2026-01-31 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51e7973b-748c-3f3b-b8ad-9ad3762729ab | -12.3086 | -57.36383 | 2026-01-31 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6f48c3b-1588-304d-bc80-44df099e5a16 | -12.30375 | -57.36293 | 2026-01-31 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60dd447d-cb6c-324e-a39c-0091f3614c68 | -11.95341 | -58.73984 | 2026-01-31 04:36:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bce6d667-8236-386b-b23a-9b93db2d9fa6 | -10.71861 | -59.2224 | 2026-01-31 04:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 3151e82e-5a5b-3ecb-b9be-d225546e8e82 | -11.98247 | -50.76049 | 2026-01-31 04:36:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a109ed16-2737-3497-b69f-cdd6c0f3e70b | -11.97911 | -50.75993 | 2026-01-31 04:36:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48a16c14-6888-384b-a4c2-9689ab6cc1d7 | -10.71787 | -59.22618 | 2026-01-31 04:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 40d9f408-25f8-37d0-a4ef-76934221f032 | -12.63233 | -48.91469 | 2026-01-31 04:36:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e5cb2cb-f6d0-3852-bad9-fa8e37af0b5b | -11.97238 | -50.75881 | 2026-01-31 04:36:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b524df5-ca3a-3ba5-89ab-749c88a0d5d8 | -11.00331 | -54.00304 | 2026-01-31 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9990a5a-0e8b-3e8d-b15c-a39ffc1fc452 | -12.63564 | -48.91522 | 2026-01-31 04:36:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 531e0f42-0e77-3755-8923-b67ca0765708 | -10.72426 | -59.22337 | 2026-01-31 04:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4f299ca5-fce3-3e76-bfdc-a09b3219cc81 | -11.97179 | -50.76247 | 2026-01-31 04:36:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ed4cde68-8909-363c-85a7-8805e775f73d | -10.72351 | -59.2272 | 2026-01-31 04:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 51fb013a-61cd-3260-aa55-3d8b039c86d0 | -11.97574 | -50.75937 | 2026-01-31 04:36:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea149fa2-d585-3855-8e54-a4b42189b9fb | -11.9712 | -50.76612 | 2026-01-31 04:36:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d783c5e-b87e-3a9c-9e8c-4735ad0404d9 | -11.00391 | -53.99951 | 2026-01-31 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34e9157e-4c00-301d-81ee-da863f9b4a0c | -20.32944 | -57.36124 | 2026-01-31 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 6def293c-3654-3626-85e8-cd385aab573b | -19.47359 | -55.46677 | 2026-01-31 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 107a8b72-ad87-3098-b02d-6bb4d2afba11 | -20.31532 | -57.36674 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| c4d02fba-78f2-3d12-9b5e-4c44a337576d | -20.32447 | -57.36444 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f634e05c-8ec4-3201-8ccf-c29acbc37b6b | -20.30983 | -57.32715 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f79c9a57-093f-36b9-b16a-57b078af0c60 | -20.26569 | -57.33049 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ba5890a-878a-3ae7-878d-618af392f292 | -20.31689 | -57.35853 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b9637ed8-fd38-31a5-b31b-f48cb97dd985 | -19.47448 | -55.46183 | 2026-01-31 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 90825ce4-e629-33e3-a958-1863592e223e | -20.32029 | -57.36354 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| b28b9cc1-c411-3cba-bb3e-548777e3fc83 | -20.29439 | -57.36225 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 514cc42b-a5d6-340e-89bc-a7ee014b065d | -20.30566 | -57.32624 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f7d8f4c1-2943-32c9-b645-1d36bf21809c | -20.3114 | -57.31898 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 92a7d234-8905-3077-9262-a7b5b3719f67 | -20.30852 | -57.35673 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7271c9dc-26f2-36fa-8165-24b0e907b95d | -16.58098 | -57.80504 | 2026-01-31 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f353127f-a17b-39bb-bf5c-37de4a921997 | -16.58561 | -57.80591 | 2026-01-31 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 714caa25-aea3-3cd8-a470-d9a0ffc8862b | -20.29779 | -57.36726 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 54d250e4-c2c0-3930-a7a2-58be7f4839e9 | -20.2936 | -57.36636 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86ccbea6-65e6-30e9-8602-8e7b5acdb7b5 | -20.31951 | -57.36765 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 573f5425-e18f-3bcd-beb5-c801edf3104a | -20.30616 | -57.36907 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 8c14b76b-43a8-3972-89b1-ef44ad96e0f8 | -20.32525 | -57.36034 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4e070ba0-c5b4-3cc9-a9bb-c08fc0dfb528 | -20.30538 | -57.37318 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 72c62be4-1d71-3202-adf2-15974831ff8d | -23.27917 | -50.31039 | 2026-01-31 04:38:00 | NOAA-21 | ABATIÁ | PARANÁ | Brasil | 4100103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7864e1b0-9407-33f5-bf07-767982c7d8bb | -20.31557 | -57.31988 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 95eee9a7-6874-3f9d-9b99-47d15727090c | -20.30774 | -57.36084 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 96e9c95c-d3f3-32b1-835c-ad749e8c83d7 | -20.32264 | -57.35122 | 2026-01-31 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8251cf09-840f-3caf-8b23-a2b3e8048456 | -22.02382 | -49.50496 | 2026-01-31 04:38:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 42ffbf5b-adc7-3d05-a8b5-738b9c24ac9a | -20.30956 | -57.37408 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 29a8c4de-ca93-34d3-bda9-181f2f8df880 | -20.32603 | -57.35623 | 2026-01-31 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3d52b8b5-897b-3153-b4b8-d471e7667145 | -20.32107 | -57.35944 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| cf09553c-c368-353b-8232-76fca73096fb | -20.31375 | -57.37498 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 22c0c780-1ad0-30b1-ae22-dac1b9845436 | -20.32185 | -57.35533 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c2724a39-43ad-3c2b-b35f-bb9eef1935b2 | -20.30695 | -57.36495 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5eb01116-65fe-3eb7-a44e-7966c4fc1266 | -22.93662 | -48.96909 | 2026-01-31 04:38:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c13aaaca-76fe-3bca-9a44-9a181758846b | -23.45552 | -46.38992 | 2026-01-31 04:38:00 | NOAA-21 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6bac2627-a0cc-394d-8b76-e68484eb21c0 | -20.31794 | -57.37587 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 7cafdf7e-b783-3a59-ad93-c53dfda9f03a | -20.31872 | -57.37176 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| fb3b2b1c-b5ee-3b8d-a325-7df01313466e | -20.26648 | -57.3264 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a5fe7a3-8495-3c85-899c-b1cfe857d3c9 | -22.94003 | -48.96842 | 2026-01-31 04:38:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f6167e6-b8f8-32c6-b50c-e3391962e1f7 | -22.93649 | -48.96784 | 2026-01-31 04:38:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 548b2457-5f4c-3966-8f23-5fe94b76e4d0 | -23.27036 | -51.20684 | 2026-01-31 04:38:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 35777c09-da3d-3fb9-9f13-9aaaa8f222b1 | -20.30016 | -57.35493 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 99a97934-3c69-3155-b79d-d6a943bc4856 | -19.47068 | -55.46106 | 2026-01-31 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 87585015-6f66-3e92-a2cb-a7353361f235 | -20.33022 | -57.35712 | 2026-01-31 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 54586a61-4dc6-3c1b-844e-d86a6ef61ea8 | -20.31454 | -57.37086 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| a4ed7c3b-06f3-3435-afcf-f8ab29f3406b | -20.32369 | -57.36855 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 46944921-b01d-3851-b3b5-bfda8c54110e | -20.3161 | -57.36264 | 2026-01-31 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| b95ba216-f7f6-3a48-80b9-9b367f7475fd | -21.83031 | -56.28354 | 2026-01-31 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bdc8f88-0698-3091-b48d-d17c86af512c | -15.79681 | -59.68691 | 2026-01-31 04:38:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22519c98-af4e-3d62-990b-3006ea698387 | -21.17903 | -56.49794 | 2026-01-31 04:38:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b67cb181-9d17-37e0-9863-0114e73e14c4 | -1.8058 | -54.4923 | 2026-01-31 04:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 6b47f952-5a09-3f6c-9bf7-ce8e7b5f4b26 | -20.3178 | -57.3644 | 2026-01-31 04:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 4448bd26-2a53-3de1-bbe9-5d146e762dc3 | -26.11513 | -53.29442 | 2026-01-31 04:40:00 | NOAA-21 | MANFRINÓPOLIS | PARANÁ | Brasil | 4114351 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eb189767-f2d2-3aee-b962-7cb169da736d | -26.11843 | -53.29509 | 2026-01-31 04:40:00 | NOAA-21 | MANFRINÓPOLIS | PARANÁ | Brasil | 4114351 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 76cd5032-d537-372e-a3ef-0e0070089ae7 | -29.54777 | -55.47295 | 2026-01-31 04:40:00 | NOAA-21 | MANOEL VIANA | RIO GRANDE DO SUL | Brasil | 4311759 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 9635ca9d-302a-33b7-9e3c-e180a0dcb7f1 | -27.36484 | -53.16496 | 2026-01-31 04:40:00 | NOAA-21 | AMETISTA DO SUL | RIO GRANDE DO SUL | Brasil | 4300646 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 12b72e61-4198-30ee-a0a2-3b7471dd3b17 | -25.44825 | -52.86544 | 2026-01-31 04:40:00 | NOAA-21 | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6161e604-d890-3de3-ad58-0a9de2d86c5f | -26.26877 | -52.71232 | 2026-01-31 04:40:00 | NOAA-21 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 627edabc-a72c-321b-9507-6b5f6604f417 | -26.26547 | -52.71169 | 2026-01-31 04:40:00 | NOAA-21 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 302b35b8-7070-3e4e-a146-464fec9cb5bb | -26.51487 | -52.19666 | 2026-01-31 04:40:00 | NOAA-21 | ABELARDO LUZ | SANTA CATARINA | Brasil | 4200101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4a5c2008-3464-3834-9fbb-f77ee045fb2f | -28.4195 | -54.9151 | 2026-01-31 04:40:00 | NOAA-21 | SÃO LUIZ GONZAGA | RIO GRANDE DO SUL | Brasil | 4318903 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 25b731b8-1114-37f8-a9e7-5c4aab55b4b8 | -1.8058 | -54.4923 | 2026-01-31 04:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 6ae0e996-96bd-37bb-8038-4daf1d49171c | -20.3178 | -57.3644 | 2026-01-31 04:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.8 |
| cc0af738-2c48-3466-a742-799da40b48ec | -20.3178 | -57.3644 | 2026-01-31 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.0 |
| cdec6069-90d2-3008-a1ab-3179644e97f0 | -2.58294 | -54.72551 | 2026-01-31 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 139359ad-39d9-3e3b-a1ff-3572f250dc10 | -3.26053 | -42.54329 | 2026-01-31 05:01:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb7f0fae-92b1-3f7c-b5d3-6efc058646b5 | -2.23697 | -47.75673 | 2026-01-31 05:01:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README5.md)
