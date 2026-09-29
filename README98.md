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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3bdeaf6-afb6-3477-bab8-674014708942 | -8.3208 | -44.1679 | 2026-09-29 17:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 280.9 |
| 7688deba-fc22-3631-a4d3-12375acbffe0 | -10.8777 | -50.6886 | 2026-09-29 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| ea3152f6-44d6-3bde-bc96-bd8269f04456 | -12.3669 | -50.2187 | 2026-09-29 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 7559dee3-831b-347d-be70-472f37b351e0 | -11.9034 | -50.6175 | 2026-09-29 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 8de89232-4ad0-328e-89b5-071a2dde205f | -11.6404 | -43.4981 | 2026-09-29 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 191.3 |
| d9691253-3778-34a3-a997-89941aed08f7 | -12.3679 | -50.1539 | 2026-09-29 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| abd5b1ec-8b32-3dbb-824e-5936c35e6e49 | -10.6505 | -50.7123 | 2026-09-29 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 51e20430-31fe-3ece-8448-1905b6623887 | 2.1082 | -50.8583 | 2026-09-29 17:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 79.3 |
| bb995e51-1b55-3dee-9866-26b81fe209fb | -11.9596 | -50.6751 | 2026-09-29 17:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 581869b7-f5d8-3490-9de1-e4d2612ffa04 | -12.2703 | -50.2951 | 2026-09-29 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 792f0392-bc2e-321b-a8e1-363a6098f6d0 | 2.1082 | -50.8792 | 2026-09-29 17:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 9520ad85-11a4-3bba-9b2b-500d3b4a4d86 | -11.8669 | -50.5147 | 2026-09-29 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| ff1cbef1-9c0c-3015-be2e-7b1af90d9380 | -11.699 | -43.4416 | 2026-09-29 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 5ed4f3ec-451f-3ac8-94bb-fdf075e2153e | -11.9037 | -50.5961 | 2026-09-29 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 6ed446d7-919f-30b3-8789-ac9026aa4abd | -11.751 | -50.6351 | 2026-09-29 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| dc6f1097-d7f4-303d-b75d-607a118f0f63 | -12.0129 | -50.9251 | 2026-09-29 17:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 097e444f-a70c-38d5-8473-ae6f6fc9f107 | -10.6505 | -50.7123 | 2026-09-29 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 350c36d5-95aa-3377-8f55-a22c89fca2f0 | -11.2566 | -43.5331 | 2026-09-29 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 313.7 |
| 4ccbaf47-2b77-305a-93ff-e415c6b944e4 | -9.9595 | -50.1431 | 2026-09-29 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 99765d0a-3cff-3321-940d-bd14550ec426 | -12.0618 | -50.2127 | 2026-09-29 17:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 73927dc7-ae21-3efa-8bd6-90c745af1a6a | -14.0915 | -46.3096 | 2026-09-29 17:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 234.5 |
| 666f0a2f-b26d-37cf-beb1-6e5af162f374 | -10.2067 | -49.9898 | 2026-09-29 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| e8bb03d3-086d-3fd1-b4d7-3c2fcfbdb90d | -10.8944 | -50.8569 | 2026-09-29 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.4 |
| c35bbad4-ca0d-3ff5-8322-17005ea77916 | -9.9956 | -50.2675 | 2026-09-29 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 1acebe6b-78d7-3a2a-b41c-327457ee5bf4 | -11.9231 | -50.5724 | 2026-09-29 17:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| ffd98f24-12e7-3922-a847-042d5085c709 | -12.1185 | -50.2489 | 2026-09-29 17:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| cc3846a9-ecb0-358b-8456-5557efa7f669 | -11.9939 | -50.9273 | 2026-09-29 17:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 8ec37f89-eb5c-37cf-a7f6-d85ffee86434 | -10.6892 | -50.6445 | 2026-09-29 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| bf1ad8a9-9865-3e3f-8e4f-2451957c3077 | -10.8967 | -50.6866 | 2026-09-29 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 99d97967-74e5-3c07-8a3b-59b9fa64213b | -12.6078 | -47.2653 | 2026-09-29 17:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 287694a4-552b-31a3-8af9-f60b55a4fe1a | -11.1178 | -51.1304 | 2026-09-29 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 7f99c73c-4d75-3923-b38a-1b0d6ff236cb | -13.3267 | -43.9523 | 2026-09-29 17:50:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 7185e618-e54f-3b52-b7b1-54d68013bc4e | -11.6212 | -43.5011 | 2026-09-29 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 266.7 |
| 9e28f284-2134-3f01-bee4-ca6c2bc60db3 | -0.821 | -49.1304 | 2026-09-29 17:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b6bad199-b0d6-3815-8e67-7f4bb69804e4 | -11.7135 | -50.5966 | 2026-09-29 17:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 5c9442d5-689b-3bce-aa09-7f5eb8b8473e | -12.2897 | -50.2712 | 2026-09-29 17:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| cd697651-d6a6-3a35-9817-03b706584a41 | -11.3922 | -43.4417 | 2026-09-29 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.4 |
| e02719be-4889-3a2f-9488-5c56151f3eb5 | -0.4889 | -49.1327 | 2026-09-29 17:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| ddefdbc8-cd27-3e54-ab29-63427ebdde4c | -11.6404 | -43.4981 | 2026-09-29 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 265.2 |
| 6c39f95c-c8c2-314e-ac97-508c4fbe37dc | -11.904 | -50.5746 | 2026-09-29 17:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 92e2a088-87a3-3853-8d34-5a57a91aa2c4 | -8.5489 | -44.0502 | 2026-09-29 17:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 96b447bf-e93e-361f-8102-819c94af7ac0 | -11.9418 | -50.5916 | 2026-09-29 17:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 3148a519-9650-3548-95e0-3511bda7c457 | -10.9538 | -50.6592 | 2026-09-29 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| e8f9ea0c-eb2f-3987-bac3-9acc460aee75 | -12.4351 | -44.1497 | 2026-09-29 17:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 246.1 |
| 9dedeaba-586e-3524-9512-fea8eaafa72a | -11.4119 | -43.415 | 2026-09-29 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| e26cc6f4-ce5f-355f-8aba-bac8767e00b8 | -14.5168 | -48.2958 | 2026-09-29 17:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 9e82ec51-0d8d-33b9-aea5-e597feb0f96a | -12.2894 | -50.2927 | 2026-09-29 17:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 2190cc61-41aa-3641-bb0b-451c59c654e2 | -11.1364 | -51.1496 | 2026-09-29 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 86e4b511-6a4a-3c87-a161-3a7f6565145e | -8.0166 | -42.8681 | 2026-09-29 17:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 38fba2eb-5d03-3cdf-a8e9-7d0719a78785 | -12.2706 | -50.2735 | 2026-09-29 17:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| d3ca8cf7-5a48-3398-a524-6a327e5f0d70 | -11.9224 | -50.6153 | 2026-09-29 17:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 871a994a-0ea4-31e1-adcb-15b05d88a8d3 | -11.3743 | -43.3734 | 2026-09-29 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| ec9b43d7-346f-3a43-941f-6a845ee7d29e | -9.977 | -50.248 | 2026-09-29 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| de56b562-057a-3532-ac71-5b94ecee616d | -10.8851 | -50.1539 | 2026-09-29 17:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| c39af904-24ea-375b-bb7c-09aae960cfe4 | -9.4535 | -41.8088 | 2026-09-29 18:00:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 95.8 |
| a3d61020-f010-3cbd-9c23-e9638a8e0af5 | -11.8669 | -50.5147 | 2026-09-29 18:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| aa52ad0e-3a04-3307-8dc2-bfdb4d68e8c3 | -10.9915 | -50.6765 | 2026-09-29 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 90aa85ac-f83b-3719-b38d-dbc414430bf5 | -9.9595 | -50.1431 | 2026-09-29 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 0e064f18-ead5-3b34-80fa-dcc472441495 | -13.3267 | -43.9523 | 2026-09-29 18:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| d9e6fbcc-bde9-358b-927b-82a4c4e4761e | -11.3743 | -43.3734 | 2026-09-29 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 2ee26077-2138-331b-aea9-de7caf6062bc | -11.3922 | -43.4417 | 2026-09-29 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| b9e4c379-c82b-355b-a4c8-47d04cbe8650 | -11.6404 | -43.4981 | 2026-09-29 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 214.7 |
| 9d424026-a81c-3c7d-99a8-4729d520adcd | 1.6566 | -55.903 | 2026-09-29 18:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 12efe44c-d92f-398f-86d8-3cbe70502f7e | -9.9956 | -50.2675 | 2026-09-29 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 1f1bc374-cd49-3746-bdd8-d8625f64a6a5 | -7.2356 | -72.4631 | 2026-09-29 18:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 02b1b45c-b635-3499-8466-9a4379f3db7d | -10.8851 | -50.1539 | 2026-09-29 18:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 660b5779-d179-3714-8157-337149060d23 | -12.4539 | -44.1702 | 2026-09-29 18:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |
| f26bab59-34ac-34f8-999b-b546beb32b2d | -12.4351 | -44.1497 | 2026-09-29 18:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 432.9 |
| 609dfe3b-e60b-3ba4-862a-669c7694edf1 | -11.0101 | -50.6958 | 2026-09-29 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 25573610-4119-387b-9e7a-d358ae415016 | -10.9154 | -50.7059 | 2026-09-29 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3ccd2049-f2b2-36a6-b20e-510b9ecf5572 | -0.4889 | -49.1327 | 2026-09-29 18:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 69224334-21a5-38cb-a247-4063eb9e6a03 | -7.8613 | -71.7654 | 2026-09-29 18:00:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 83905b3e-e6a9-33b9-811a-d050f0166494 | -9.4344 | -41.8113 | 2026-09-29 18:00:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 156.1 |
| f30bcc6a-e081-384b-9de1-5e327e633fd4 | -11.4495 | -43.4566 | 2026-09-29 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| faa1597f-b5d9-3a1d-b130-379052c3a1e7 | -11.2758 | -43.5303 | 2026-09-29 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 1f5f1a5a-41e1-3463-995f-9c24f6d13c48 | -11.4119 | -43.415 | 2026-09-29 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 22c60bf5-ae46-3881-8c82-19bfe696104b | -10.7056 | -50.8341 | 2026-09-29 18:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 0c64cb48-0efc-316b-a5f0-d33d88358c8d | -1.0238 | -49.2348 | 2026-09-29 18:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 44e52bd8-3eb4-3353-901c-4804f31c6cc8 | -7.0166 | -44.6184 | 2026-09-29 18:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| e43da5e2-4413-30f3-bda1-d8e70dbd1630 | -11.6212 | -43.5011 | 2026-09-29 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 249.7 |
| d8a5e2b6-2b7c-38a9-9b29-b30f7b872328 | -10.2067 | -49.9898 | 2026-09-29 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| a2b317d9-b8b2-30c4-b516-1017440ec88f | -11.9034 | -50.6175 | 2026-09-29 18:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 86404fd5-6386-3a01-b66c-d9e39c0070d5 | -10.207 | -49.9684 | 2026-09-29 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f7dc6dfb-608c-3ed2-9bed-d596351566db | -12.2706 | -50.2735 | 2026-09-29 18:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 16e3175b-17d5-37fe-b872-e7e14a62de1e | -10.6505 | -50.7123 | 2026-09-29 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 38c1e3ea-bdad-36b8-942e-5fb838ec983f | -10.8944 | -50.8569 | 2026-09-29 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 33e58d53-f532-3714-88b0-704a0de47df9 | -11.9037 | -50.5961 | 2026-09-29 18:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 1373a392-68b0-3953-8ae2-d4bdc994d82d | -11.4791 | -49.743 | 2026-09-29 18:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 79a2320f-d464-3691-b40b-486db5b1208f | -8.3617 | -45.4013 | 2026-09-29 18:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 60.5 |
| fb22efe7-a5e9-330b-bc49-10e51d46352d | -10.9349 | -50.6612 | 2026-09-29 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 66d242f3-a931-38c6-9d0d-50b127452113 | -6.9795 | -71.755 | 2026-09-29 18:00:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 687b63a9-4456-3336-9145-e2ef29ff4e46 | -12.6078 | -47.2653 | 2026-09-29 18:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 7da193fa-ff2b-3615-8ad2-9121c19a8a05 | -11.2758 | -43.5303 | 2026-09-29 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 10f81ad0-f723-3674-b903-7698edb929db | 2.569 | -50.848 | 2026-09-29 18:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 86013a0f-6eee-3a72-b291-523b77b6d38c | -11.6596 | -43.4951 | 2026-09-29 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 6ce19a84-06e4-3574-9e7c-c67f1a6166c3 | -8.9294 | -49.7706 | 2026-09-29 18:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| d1e950bc-be8b-37c1-bfc7-38de538105ba | -12.4351 | -44.1497 | 2026-09-29 18:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 260.5 |
| 09a757cb-829d-3e46-b10e-867853cc06e5 | -10.9915 | -50.6765 | 2026-09-29 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 920dbd1b-45d7-33ee-900f-33ae8def63ba | -12.4539 | -44.1702 | 2026-09-29 18:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 72fa0c16-5d16-38f8-a233-d7fd3b1b4b86 | -10.2067 | -49.9898 | 2026-09-29 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |


[Clique aqui para ver as próximas entradas](README99.md)
