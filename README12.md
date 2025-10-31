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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 297e887a-0c9b-3e0c-8ab6-0e996817f56c | -5.11447 | -43.29403 | 2025-10-31 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e4b5d336-2edf-3681-9a19-56b7ee3d0efa | -4.70035 | -46.49789 | 2025-10-31 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17eee1ce-ad52-3b39-b25e-dcb5307ea4e5 | -9.8597 | -44.8511 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 43fba37c-d436-3d49-8921-e10437109685 | -5.0397 | -43.61251 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a8feee6b-8733-3f46-bb24-2a66dbf2b6e1 | -5.88295 | -43.19803 | 2025-10-31 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8d6bc792-1440-32af-9d73-286b01cf9334 | -5.41962 | -47.94115 | 2025-10-31 03:47:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77111e99-3dc8-336c-a563-e43d3a116493 | -7.08167 | -44.93737 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eeae20e5-5c17-3302-beed-12873871ebeb | -8.09648 | -45.14208 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ce6a7e0-6149-32c3-8ade-80f1fb44fd0e | -13.90457 | -47.35377 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd7b6379-6da5-3b52-9358-6c9620331060 | -7.88373 | -45.69131 | 2025-10-31 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44b9a98b-3a9d-3098-8c13-0b45c9bd8f14 | -6.93088 | -46.01765 | 2025-10-31 03:47:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bc7817b-99cb-3c19-be9e-e97ee0682f24 | -4.86729 | -44.65031 | 2025-10-31 03:47:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f6e9800-0c76-3a15-9243-a9b063177033 | -3.98765 | -43.42273 | 2025-10-31 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d154abb0-a0ec-3d43-a0b7-9368d24207c5 | -13.90049 | -47.34475 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c51c1f5-cb89-3e0d-93b7-4ca5e855afd7 | -5.63903 | -41.08755 | 2025-10-31 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f9e6bf0e-939b-3728-8250-6b2a98db7578 | -5.79215 | -43.73618 | 2025-10-31 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78606447-6c8b-34a4-8062-e81e5a513512 | -6.36315 | -40.97301 | 2025-10-31 03:47:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c3350f39-ceba-3db9-b7b2-6059882ca59e | -5.23244 | -45.47688 | 2025-10-31 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8ad626d-3c96-3e78-814e-2f5b01e6f389 | -5.96136 | -45.55502 | 2025-10-31 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0ce006e-96d7-3d0c-91f2-22d3eade3945 | -8.04675 | -41.1101 | 2025-10-31 03:47:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ecce8557-a123-3a63-b69a-287ce4c2ac01 | -7.92169 | -46.79352 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3811835c-4434-36e7-9f9a-a4d54bd0e93b | -13.53648 | -47.42582 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a051857a-d5bc-364b-901c-61f2580fb4af | -13.5235 | -47.13208 | 2025-10-31 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6e56280-b008-3b9b-83be-d8c5c6eacbeb | -6.7673 | -35.44809 | 2025-10-31 03:47:00 | NPP-375D | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9a2298b2-c0af-3ab1-acec-124659568174 | -16.37536 | -45.24851 | 2025-10-31 03:47:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 15cc4969-c40e-3d24-aa59-37fee8337617 | -7.93362 | -42.24152 | 2025-10-31 03:47:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f55afed2-7cb3-35ee-9e08-7a2e06c84747 | -8.16888 | -45.49383 | 2025-10-31 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d554619-2f37-38d0-974b-dd85f3d29330 | -7.43784 | -46.889 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f586c01-1c14-386e-83ff-f33e5f363602 | -15.40738 | -40.86504 | 2025-10-31 03:47:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9fcfa134-47b5-365e-ac71-028cdc7d96b7 | -5.28318 | -45.41933 | 2025-10-31 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9091c505-3575-37f7-b226-6cccbb11742e | -4.35767 | -46.7776 | 2025-10-31 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd26de73-d7dc-3a3c-97ff-efe9db2ff8b6 | -10.932 | -44.1582 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a7ff40a8-5306-34f3-984a-e042d478b2af | -7.04818 | -41.47776 | 2025-10-31 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d8a3ea1f-3ad2-322c-b03f-1caa8ac6a29d | -9.86252 | -44.86502 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0945a70f-4265-3968-a62d-e26af9d78593 | -9.22053 | -45.58091 | 2025-10-31 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67a0183a-412b-35d4-80fe-3bace08a3d50 | -10.88315 | -44.36657 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3407b7e4-54c3-3025-b6a2-1639981591b5 | -4.43169 | -43.71509 | 2025-10-31 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6bb1c2c-b7dc-3338-a994-67fc6c10f9e3 | -4.46056 | -45.76162 | 2025-10-31 03:47:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e7c8e0e3-0cff-3e4c-9933-1dffa9ead291 | -4.67122 | -45.8145 | 2025-10-31 03:47:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65199a6a-732b-3fbd-a84f-ca3f7d12f567 | -9.51462 | -47.26432 | 2025-10-31 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| feb861b0-8443-30f2-830a-3bb3047d86ed | -13.27115 | -47.76109 | 2025-10-31 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58e4d75c-4b8e-3c89-979e-cf23d6e2ec9d | -6.40633 | -39.74083 | 2025-10-31 03:47:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6be3a377-3f67-35a2-abf5-3e0875a6a8ea | -4.78531 | -46.88239 | 2025-10-31 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f0e226c-d8d3-33b2-96e8-c50786bc5766 | -13.38651 | -47.33712 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed67fcee-fa6d-381d-99f0-9c8ed1028740 | -8.94904 | -40.86644 | 2025-10-31 03:47:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 881a9676-e1f6-39b1-96eb-c5596fe3c2fa | -12.93929 | -47.92977 | 2025-10-31 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7b3f3cd4-88a2-38f4-b9f4-dd4d714fe895 | -11.02725 | -44.64758 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5cc26006-0912-378c-a118-5bf831aaabee | -11.05099 | -44.29219 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e075de0a-9b71-37da-bfea-a05ccbd55793 | -13.67744 | -44.71762 | 2025-10-31 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 957b08b2-98d4-39cd-bfcc-df4e24fe87c4 | -3.53457 | -47.55404 | 2025-10-31 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c6065bfa-4c7e-3388-a175-52b740411b8e | -5.85646 | -44.71046 | 2025-10-31 03:47:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 922aa3b8-06c4-3971-a7da-6f5c0cbd9784 | -5.862 | -44.71127 | 2025-10-31 03:47:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72704981-96bd-3e56-8575-ae1b2f345f21 | -10.84629 | -44.9317 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e10b91b1-6f32-3037-9098-b9842b6edd1f | -5.33194 | -42.66796 | 2025-10-31 03:47:00 | NPP-375D | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cd25073a-5393-3b3a-8c31-d98252f425e1 | -9.87925 | -44.86166 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b1df0b3b-e151-358d-aa97-9809667baf91 | -9.72982 | -48.02157 | 2025-10-31 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9dc0d2d-8f66-3a6e-b00b-dd2440425723 | -7.92776 | -46.7947 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a1183e0-8a53-38da-94dc-604a07767761 | -14.65519 | -44.2726 | 2025-10-31 03:47:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf4fd741-b289-37ec-aafb-7eefb6dbf5d7 | -7.04044 | -41.47425 | 2025-10-31 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 948d4a49-3cf1-3154-97c1-344fe4fe7b35 | -4.67653 | -46.52221 | 2025-10-31 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a87f7df0-4531-358d-9fba-0fde36719f41 | -14.00071 | -44.01899 | 2025-10-31 03:47:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49c552b4-d93f-391e-8261-86c8aa9ce2d7 | -4.78627 | -46.87714 | 2025-10-31 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 068f9dd2-c09f-3714-9576-4d7f5e00a2ad | -9.88812 | -47.45287 | 2025-10-31 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc7bc37e-67e8-392b-ac34-613a9cfb4fc1 | -10.50757 | -42.4058 | 2025-10-31 03:47:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| c29dfc02-fd33-3887-9576-d6a7fbe9b1ac | -5.32963 | -42.66864 | 2025-10-31 03:47:00 | NPP-375D | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 44d3602f-585c-3a82-abf2-27351cde4a95 | -4.55768 | -45.63171 | 2025-10-31 03:47:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 918436e0-48ff-3127-852f-abce84a0dbed | -4.79618 | -46.46803 | 2025-10-31 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6a9b458-e147-3b26-bb4b-7a0564e82949 | -9.7332 | -48.03839 | 2025-10-31 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fae88a15-93be-35cb-b86d-fc17d4b8c99c | -6.01376 | -41.9743 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d68d37da-fe6f-38b2-b8d6-4d60d4b3c769 | -5.1125 | -43.29469 | 2025-10-31 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 83188310-c71d-36e8-b275-daf542b7fd2e | -9.73678 | -48.02616 | 2025-10-31 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2947c73d-0901-3746-a37a-68b1972511f2 | -3.81444 | -45.05355 | 2025-10-31 03:47:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d65a40a9-9daa-3124-9f0a-29b12b52c1ce | -12.93842 | -47.9341 | 2025-10-31 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 59fd5aea-f09c-360b-9b87-788af75099b3 | -6.01455 | -41.96973 | 2025-10-31 03:47:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c375151f-c4d2-3980-a2ed-e80679a319a9 | -6.53273 | -43.70941 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e66ec6b-bf58-3197-b7ef-653a3aea3117 | -5.96062 | -45.5592 | 2025-10-31 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a900a83-5caf-3148-a4f9-9d450ff3d9c5 | -7.40468 | -39.83074 | 2025-10-31 03:47:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6280374d-34ab-3111-ab2c-0a206545b86b | -8.10711 | -45.17716 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d8f41fc-ad2d-3ca1-a3f1-4cca4406d29e | -5.0381 | -43.62198 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f1612d8b-4dac-3efb-9bcc-3e83e432c1c4 | -11.02588 | -44.6478 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2dbe859d-5f96-3df2-9990-3edaa19f0e6b | -11.01372 | -43.87576 | 2025-10-31 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 938457d3-dda3-370d-8665-0b63babe3c58 | -8.10163 | -45.1762 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f7a59fe-8d51-3c79-803b-49481896467a | -6.19771 | -42.52275 | 2025-10-31 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 694820ec-d3dc-3002-b996-d86889b0b6ec | -5.7897 | -40.8107 | 2025-10-31 03:47:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f00fcb18-e2d3-3a42-b49e-29f39b7be2d8 | -10.95366 | -44.68002 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4e038fc-dbe0-3092-a605-5d528efbdc54 | -10.84115 | -44.93078 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c240e788-adc5-349d-94d8-72556dece065 | -3.98658 | -43.4291 | 2025-10-31 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9365345b-3b01-3089-b044-d82c49c7a375 | -9.35012 | -46.59723 | 2025-10-31 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0dfe6010-ddd4-350a-a7e1-d7d95d047242 | -10.84686 | -44.92858 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a79198b7-1d21-3424-80ed-3e1c33f7b4ee | -7.36021 | -44.63864 | 2025-10-31 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f93bd87d-87c9-3c60-9407-ebcaf9a15384 | -13.3858 | -47.3407 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7580b0a7-dfcb-3178-8f7d-74984d179e84 | -5.45979 | -40.86927 | 2025-10-31 03:47:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8bd26748-613b-367c-a51c-53c8c8e6be7e | -6.25503 | -42.56025 | 2025-10-31 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 47b92f43-ac8f-3c1f-8d0e-2753513ea405 | -3.48215 | -45.86492 | 2025-10-31 03:47:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e96c2c2-14d8-3539-8d87-a89132593b45 | -5.41853 | -47.94711 | 2025-10-31 03:47:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 917cfeae-3168-3273-a89b-3e6feab161cc | -7.37716 | -46.22088 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9829db70-92bd-3ae5-918e-993195de0953 | -13.88439 | -47.33679 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 24050cac-e862-3705-87d1-e66f3594e928 | -6.20334 | -42.51822 | 2025-10-31 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 5bdc97d8-2dcf-3abc-aade-ea14b06e7f75 | -5.45919 | -40.87283 | 2025-10-31 03:47:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3b66dd4e-6433-3ce0-ba90-047e4ea02518 | -9.8723 | -44.87027 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README13.md)
