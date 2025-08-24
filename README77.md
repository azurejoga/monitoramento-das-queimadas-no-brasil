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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 630360e0-5c54-38bf-886f-9f5a1ae5a802 | -9.18076 | -59.59074 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bec1ee65-33cc-3aaa-9b98-d8da551ea3a6 | -9.849 | -63.3262 | 2025-08-24 05:25:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2e00ad3-a520-3050-9b17-bf6d40785311 | -9.17002 | -59.59282 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4a300f3-a29b-36c9-8788-c85738bc77b6 | -9.15803 | -59.51185 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9b1c5ce-ec13-3014-91c4-e07466340e89 | -8.00135 | -63.08471 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b2310a6-5923-3e17-8476-67b5c8eb69cb | -8.90021 | -62.41066 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90ff5d06-8e1d-3b67-ab58-446ba63042fd | -9.17287 | -58.30874 | 2025-08-24 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0db2caca-cba1-33f2-a121-95adeb8edc44 | -9.27228 | -65.9077 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a32eef25-ab43-3d3d-a4ea-ecdd3c73c990 | -9.19901 | -60.76578 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7495690-71e9-3710-9a7c-1a8202614ff5 | -9.19713 | -59.46111 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca9969d7-9dcb-3818-9dbf-37d2caf9e434 | -8.13385 | -62.87109 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f5b5189-56dc-3dfa-bc9d-951e9174d5b7 | -15.31983 | -56.15911 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6938a3a-84c9-3352-ae02-d2fa092ebe51 | -11.54925 | -51.90243 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4cfd62e-f677-36fd-ab5f-62575aff6704 | -9.20514 | -60.79184 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5e7b9ffd-b1af-3355-8ad1-0d855c915e85 | -9.14942 | -59.45373 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a538ab4d-f066-3071-af4d-0f9cd6346eac | -9.81583 | -64.26833 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5902595-5236-3746-b4f6-84bca7388e55 | -9.18699 | -59.61802 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c07e57cc-8137-3202-a930-c15b9068f900 | -9.20053 | -59.43886 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a1bb587-09a6-3ae3-b5fe-b96193782770 | -9.15687 | -59.49654 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 002c7932-295a-3fdf-af7e-ae2d17a12478 | -9.19095 | -59.61488 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eeea7c95-9ee9-3be0-8968-a692c818c397 | -9.15114 | -59.46539 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 29b5e973-e19a-3016-a9dd-cbb7c2499955 | -9.24995 | -60.48262 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05b5ad50-3b9c-3ff3-90b4-0a9b493f23c0 | -9.1608 | -59.47068 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a047b325-caf4-3566-9c6d-c71d346a6733 | -9.15679 | -59.45107 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 27ebc7e4-94ff-39a1-83c8-9e61fb7160b0 | -9.94164 | -60.17887 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7b7dcf5-cb80-3da0-9622-4c800305daf1 | -9.1489 | -59.48017 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7a2adcd-32e3-32e5-83ae-dfa84030eebc | -9.20904 | -59.61017 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2574cbde-893b-306f-8cef-27f3fc610835 | -9.2494 | -60.48614 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8eb18434-599d-383d-902f-ea83a162a333 | -11.32052 | -47.86492 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 29759f1c-f2a4-35e2-8a01-b47e35472368 | -9.95787 | -60.18509 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eaa1cc5e-44d3-3dd2-a113-032fc98b7224 | -9.64875 | -59.64603 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa906f53-6d40-3e9b-a8ed-3a91fcd0ba1c | -11.54369 | -51.85598 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 162d7354-ec6a-3cfc-99c4-5ffca7dbfe9e | -11.54323 | -51.85969 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1b82c96a-4424-36c9-89fc-9110035d3065 | -9.65271 | -59.64291 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe4d5607-6454-3cf7-8355-42e38b16dff9 | -9.95451 | -60.18457 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2014bc0f-e481-3d86-b412-351f00a4b627 | -9.15627 | -59.47755 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| de4f4053-94fe-3e94-aaed-83ad6b6e075d | -9.01721 | -65.39031 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 13cfd4e2-45b3-3501-8994-fbebeab33841 | -16.79256 | -51.35255 | 2025-08-24 05:25:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 015697b8-ce6f-3530-9377-1a0ac72a2230 | -9.79751 | -61.21533 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2a501a9-aee9-3ff6-a2f2-1ebd2cf34925 | -9.24106 | -60.47399 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a1568e0-3f4e-3e2d-8ca8-5f7dc4b038bc | -8.93422 | -62.43458 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b474985-7242-3010-b1ec-044618a4b3ef | -9.14829 | -59.46115 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1709feb8-8718-355e-a8cf-2854cfd7e77f | -9.51588 | -60.56062 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 597b2952-08ad-35da-8c96-87efb468d964 | -11.3242 | -47.86668 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e1d2abe7-884b-3713-8981-427d488ac034 | -8.96563 | -60.49938 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 678f3ad9-1afa-35dd-a421-0b6bd8a16c13 | -9.14946 | -59.47649 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 29bf0573-3d64-3bbc-98fd-5e4eb50f0ba7 | -8.6094 | -62.59704 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 73dfac59-ad94-3761-a23b-e6097bd71193 | -11.53714 | -51.86301 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b7e2fcde-3975-31b3-a9ff-77a9b219a9af | -9.06675 | -65.71901 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4aa96dda-9424-3942-bb69-496e4f0eb94d | -15.32367 | -56.16408 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60f34cbe-5f14-3134-bfb8-f06eea288352 | -9.00681 | -65.71883 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ea30dd6-2ffe-3aa9-9c98-56be382c86d7 | -11.30917 | -56.26819 | 2025-08-24 05:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0779995c-07ad-3898-ad92-397cf9e88fdb | -9.94499 | -60.1794 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67a712d2-5b8a-38b0-9960-9b2bb17fbaae | -20.35295 | -51.68579 | 2025-08-24 05:25:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 670bfb42-a2e6-3c7a-9c15-ae086cd5b4da | -9.1693 | -59.46061 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 942ea932-1832-3bfd-8b46-2639af217b45 | -20.35342 | -51.68056 | 2025-08-24 05:25:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4c00401e-7ce5-3c63-adae-1269c248c2eb | -8.92693 | -62.43708 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8673783c-99b0-3d55-b8d4-1a782fab4430 | -11.5376 | -51.85924 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ee1aefb5-7ddf-3b2a-8fbb-195d48219cd7 | -9.94721 | -60.16499 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bcef4ec-82d5-3ff2-9685-001f6d3d3d06 | -10.34992 | -58.60267 | 2025-08-24 05:25:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3355e3c5-b01f-3e24-a007-65bc19a76b5c | -9.19683 | -60.77977 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| add25dcc-9fcf-3bea-ab57-40a0f625b4fd | -9.12403 | -60.32943 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 816aa6f6-1f1e-313f-9bf1-443357bdf92b | -9.1689 | -59.60015 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ebcdd41-d528-381c-b234-6732b7210b00 | -10.10538 | -57.76518 | 2025-08-24 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4aff718c-7618-376d-94d0-1e2e2954a736 | -11.54319 | -51.90559 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| accc45f0-0b66-3b69-bfff-65917becfcce | -9.15286 | -59.47701 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c19069a1-fab8-3791-b83d-d2e57ccbbfca | -11.73592 | -51.69604 | 2025-08-24 05:25:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3626ae03-827f-33a3-a46b-914b5f18464c | -9.10103 | -61.43225 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30436e6e-c13c-33af-ad34-2aebca4bea54 | -11.33259 | -47.85597 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6c71be2b-672c-30a4-8a90-49f954df59e2 | -8.91292 | -62.43848 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6946813-ee7b-3ca6-8314-db25adce3fc1 | -9.84984 | -62.84613 | 2025-08-24 05:25:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c4aecb1-0bfa-3d5b-ba22-aef4ae5e5e67 | -9.00851 | -65.70894 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bf0d4cec-d7e6-3638-a387-5a9b53bcd9bf | -8.99905 | -63.63702 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aff8a63b-852d-3e16-b6c3-4c280aa779ed | -9.24607 | -60.48561 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8619478-3cfb-3cf4-bc06-b59250da8969 | -11.53113 | -51.9115 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2c60cb1-f849-33a8-a1e8-ed6d472f1ac6 | -9.24384 | -60.47804 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ced2a679-e4ce-35e0-8745-d79e710871bf | -9.02876 | -65.70741 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a325c4c4-8384-3582-b21c-da564dc26a8a | -9.02622 | -65.72223 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad3127c7-3c28-3d26-a5be-53e4620c30d9 | -11.18005 | -55.02285 | 2025-08-24 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5c52894-feab-39a3-8c0b-022c95086b67 | -9.17479 | -60.81211 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d606a8ee-3ff1-358b-8d8e-e045553503fd | -15.32347 | -56.16191 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aebb8ede-5a0a-35cc-b028-ccc35f01ebbd | -8.60603 | -62.59649 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bee0210e-48a1-36fa-ba19-4ecc9efa7c52 | -9.14717 | -59.46857 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c872c67-15ba-3ea3-94cb-7f087a74c243 | -23.10392 | -49.9746 | 2025-08-24 05:25:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 071119bd-afc6-3e73-a371-1dbe159ed1d8 | -9.00718 | -65.69352 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 90fbeb89-7731-3ab5-aed5-f21ee62a0de8 | -8.13445 | -62.86737 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81084f9b-a52d-3080-9655-1dd561b2c845 | -9.95285 | -60.19537 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cc2171c-5905-3928-8993-c349a544388d | -9.15571 | -59.48123 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 29893985-4562-3c4c-b35f-30be0675a0fa | -8.90563 | -62.44098 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10b8c5f8-e884-3c87-bf1c-ad0054884707 | -9.6487 | -59.64275 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d06ccb6-4ba9-3fb4-b245-4e23da3dd6e5 | -11.5418 | -51.8712 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d48a1bae-5270-3359-91a9-c471cfa4453e | -9.95116 | -60.18404 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ef68f37-82ca-3e3b-ba81-8c5410990280 | -8.89072 | -62.40545 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a25e787e-3881-3d58-a6d9-e69df619f192 | -9.80192 | -61.20889 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 351d0cdf-a530-31d4-b949-6de82640394a | -11.51386 | -51.86751 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb570964-920b-3141-93cf-fb7e6d82b4ce | -9.17555 | -59.46537 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2bad4aff-0db6-3211-934e-9116fec7a4b9 | -20.35201 | -51.69631 | 2025-08-24 05:25:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 45b64b5c-90e6-3320-8243-a45b21b2b9fc | -20.35925 | -51.68618 | 2025-08-24 05:25:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 595d1f0f-5a65-3e95-aee0-ff598c95f3c2 | -9.20459 | -60.79534 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5a5de5c5-ca3d-398a-ad43-acfa9020c58a | -9.17896 | -59.4659 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README78.md)
