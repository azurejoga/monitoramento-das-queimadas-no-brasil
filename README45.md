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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15461d7d-4353-3b96-86e5-c2ce0ba95b41 | -14.03314 | -54.01876 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcf2e908-79b0-3ff8-99eb-42aac567a139 | -11.15549 | -50.59034 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 120380eb-761b-3ba0-9263-de4e9215aace | -7.30199 | -60.60482 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ee75315-d050-311c-b3bc-a0808c5a93f8 | -10.98987 | -50.52206 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a8e4a122-50cf-38de-9332-6b8296e0f3c3 | -16.34379 | -50.9762 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 390ef287-2513-3ee0-bc96-38b0fe0a390f | -11.34395 | -45.15749 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1f78526d-9127-3296-9f61-b72c81fbd06f | -7.31613 | -60.60779 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7ac9ebcb-99d8-3dd5-9a1d-b259f71283c5 | -10.73365 | -54.04612 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 913a5ae5-de26-37cb-9d48-cce0b3087334 | -11.16442 | -45.05131 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b721e87-f34d-3e81-8277-05a7e87e61d4 | -10.76711 | -44.85658 | 2026-08-30 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 90c28bbc-5e9e-3d66-a085-eda06235a2e8 | -12.93519 | -45.91129 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9d1305f-6632-3a05-af42-4c3c8208bb4c | -9.84697 | -60.27196 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aea49233-8a66-3b1f-b942-56f061958375 | -14.23034 | -52.84555 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6af273d3-ea06-3877-8f13-5fccbcf25fa7 | -11.71095 | -54.52903 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2854e60f-aa3c-30b4-8979-fe3577035b98 | -12.29824 | -47.63871 | 2026-08-30 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc809cfc-7c05-300b-a916-d39442172810 | -11.52671 | -45.55259 | 2026-08-30 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6b89241f-f1d9-3ac5-aed6-4cba039a1812 | -13.3564 | -46.92117 | 2026-08-30 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5bce0bb2-70f2-3e22-b06d-51b8e0a408c7 | -12.92376 | -45.87037 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5348913-994c-37c2-ad57-fbd0f614728f | -13.39818 | -51.76277 | 2026-08-30 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1bfd5dfb-1332-3edc-9642-fc2cff2c2c76 | -10.56806 | -59.61022 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a9034b0-7ab4-3035-b9df-efaaf75ef159 | -14.58828 | -53.07615 | 2026-08-30 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0c38172-9fc7-3f1f-949b-7f1f50dc211e | -14.2802 | -53.1951 | 2026-08-30 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0640f127-319f-3299-9390-155105e66b4a | -9.31747 | -47.62928 | 2026-08-30 04:34:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dd654eb-90d0-3379-b798-8df8c5e65288 | -11.19614 | -53.99432 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4ec8f80-3e1d-3eb5-872f-347c5e189821 | -9.15686 | -59.52058 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74f848ac-62a3-33c0-93a8-f0434756f483 | -15.10465 | -48.16689 | 2026-08-30 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 550c00ab-04ef-3a0c-81ad-dc90fc48a453 | -11.34046 | -45.15699 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6c03c473-415c-3712-84d7-ad332bf3d6b7 | -14.76287 | -48.73824 | 2026-08-30 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9ef9ba8-815b-3fe6-836c-1e8f28225e96 | -9.7654 | -48.16437 | 2026-08-30 04:34:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ff0bbd2-59db-33e7-8538-332a73f4355d | -10.74936 | -54.03535 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 740b2cbf-663a-305f-8a64-22f4fc88806e | -10.74788 | -50.86909 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f13b02a0-2c95-3733-9b89-aafaf7d8d9ef | -12.92258 | -45.90154 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00a8cdcb-b28d-3158-b687-87c2252f2325 | -11.29155 | -54.04256 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3c8264e4-c284-3407-b693-cc39cdbb8e08 | -14.19375 | -52.86771 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 28de8c68-1c17-3608-b4ed-bf0727b52937 | -10.75339 | -54.0634 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a8ac2b2-7e30-3f4e-9110-57e033d7d37b | -10.94907 | -43.02491 | 2026-08-30 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 974e1599-2df5-3961-b7f5-7a1304e751ae | -14.1522 | -52.80838 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b01e756-2d48-3c9f-b090-1673c915d568 | -11.18713 | -55.11057 | 2026-08-30 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d514b7b4-db1b-389a-834a-e54931177ddb | -14.20319 | -52.85957 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10f4f626-0501-324f-9613-08f2b5ac36d8 | -11.24657 | -45.32318 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f624f6f8-ddbd-3b08-aeae-17c21c41bfea | -9.70963 | -60.7449 | 2026-08-30 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f889bac2-ab25-3561-bf86-54534bfc2496 | -14.33749 | -47.22847 | 2026-08-30 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76210e79-60f9-3d7d-935a-39c957adca67 | -10.75104 | -54.03322 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ecd08729-2e32-3667-b13a-4135f54a3f27 | -11.81702 | -51.04765 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 7b66ab86-1a5d-384d-8903-f0f31e8bf02a | -17.41972 | -42.62726 | 2026-08-30 04:34:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 332e1429-8d6b-37c6-8d3b-05448d1f42e2 | -14.20618 | -52.86546 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b177c26-37f2-3521-aad5-9658464cf426 | -9.88404 | -60.27572 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3eb8683c-0442-38bc-b8c8-0ec99271f775 | -11.66473 | -46.73922 | 2026-08-30 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b78d650-5066-310f-b5fb-98dfddc928dd | -12.89449 | -45.87763 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a64ef29-8c29-3f5f-9ea9-6b7e400f191b | -11.57114 | -44.03489 | 2026-08-30 04:34:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4fac684-54fd-3fc5-b458-d7a3926a3578 | -14.41226 | -52.54866 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 97b20c36-b7ca-3a2d-8750-31651e7287bf | -10.75948 | -44.85949 | 2026-08-30 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9a7f3c1e-cbd7-3e97-be3f-191d0f69a017 | -8.61185 | -54.77616 | 2026-08-30 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7fffcd17-0389-3e06-ae28-fc7560df1249 | -11.26296 | -45.06991 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a247de2-8f53-3b80-93c3-e9b41bf3c34d | -14.33414 | -47.22793 | 2026-08-30 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d52bee4d-88d9-3710-9347-ce7343e38879 | -10.81465 | -50.5111 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af2187ed-71e3-3cb4-9e18-78f45f5d8d8a | -12.80411 | -46.45385 | 2026-08-30 04:34:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 90ea7c20-5dbe-355f-97b7-51aa0ffe85dc | -8.50851 | -55.29555 | 2026-08-30 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3d04d24-efc0-3330-9211-db9dad74f377 | -13.83438 | -54.10551 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97d1a46d-e55b-3358-ae49-1e4530d2d8d3 | -11.36374 | -45.16848 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a8cf334f-9a06-30d7-94be-c6e1ac033caf | -8.50559 | -55.28307 | 2026-08-30 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16371d06-129a-36ac-99cb-810362b8d7b8 | -9.68895 | -46.54661 | 2026-08-30 04:34:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95417098-4f35-3645-ac21-a70f1f110528 | -9.83171 | -47.83509 | 2026-08-30 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ba6fb32-c188-3f36-8f5c-3e8224c3945e | -10.75662 | -54.04573 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1156267a-918e-31e7-8d8c-ea3bcb3025f0 | -9.1586 | -59.51228 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e7d355a-132a-3966-a39e-6e484db0706a | -11.16671 | -51.3186 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcb96fd5-1363-3694-8273-f0cc697b34db | -17.79226 | -39.70611 | 2026-08-30 04:34:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e839648d-39de-3726-9cf4-2df84d370366 | -7.29489 | -60.60345 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cb034a2-847b-34e5-948b-080fc9ef7d5d | -10.78605 | -45.33716 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fc3031b-3b87-3590-8694-6a3fb218d5c8 | -11.4857 | -45.0533 | 2026-08-30 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5208f024-b319-3d66-8e6e-290f881ccc08 | -7.32806 | -60.60228 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef6e7f87-1fb2-3cb8-b093-934dac62bdbb | -9.17377 | -59.63925 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fdd06fb-6cbc-3848-87ca-dce0a452ed11 | -12.91803 | -45.86162 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40ad42cb-e65d-3b54-be65-188559def941 | -10.74562 | -50.83768 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc67de68-0e9d-3de5-a6cc-179d947fc331 | -9.4262 | -51.58615 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f6d5fac6-7810-3a91-ae60-857f28002ddd | -8.60609 | -54.78048 | 2026-08-30 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 44c2ae80-d0ed-3aa2-80eb-509f27038c74 | -11.34254 | -48.37153 | 2026-08-30 04:34:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 563bcafd-0ade-32c2-b6e0-a488812f79f2 | -10.7546 | -50.69448 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6c93fb1-4e7f-360e-9dbd-cd1b0804e3e4 | -15.12249 | -53.58133 | 2026-08-30 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f729017-c51f-3026-874b-fc1d67e80c77 | -12.23777 | -50.51894 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4ba30ad-b011-3909-9de7-73d8ea6df4ed | -17.51283 | -44.21994 | 2026-08-30 04:34:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f98513a8-4cab-3a30-a3ba-5ee4dbec3f78 | -11.34863 | -48.3762 | 2026-08-30 04:34:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b67d35a5-daec-3284-9dfc-9d02d066f368 | -9.19867 | -51.54539 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 98420e08-89b0-35c2-a7c9-e9dc3812961a | -12.89736 | -45.88199 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c94adc77-6464-3a4b-b883-67e06b489f00 | -10.74818 | -50.86784 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 265b014a-c718-3758-a086-331ada666aec | -10.75689 | -50.88266 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e193453-2818-3774-9112-19ff720571e5 | -10.14287 | -45.7006 | 2026-08-30 04:34:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5a5a73d-faf2-3924-8d76-d9324d0836e9 | -9.89191 | -60.27121 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9f41c583-a9b5-3606-ab1b-0cabdfac6ab8 | -11.21744 | -45.07969 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b40f0bee-5f86-3c17-8b0f-07ed1792ff23 | -8.50351 | -55.2946 | 2026-08-30 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b684e04f-bafe-3f88-a020-d01c09a817d3 | -11.16236 | -51.29937 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30a65c91-99b2-3945-bd31-545e3eb5209f | -14.02896 | -54.01799 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f009a47a-7806-3309-b858-b78ba6beadb7 | -9.88951 | -60.28301 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 08df06e3-e789-3792-8e05-1262f2c5f3ff | -14.23418 | -52.84649 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55c4c21a-6314-3d7c-b364-d371bdab7e9a | -9.67242 | -55.06731 | 2026-08-30 04:34:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e9ac3540-6b41-35fc-98c0-20bf35d0c8ab | -11.18953 | -45.05102 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b98c017-885f-3300-9292-0dfae0f81a99 | -11.03646 | -57.2513 | 2026-08-30 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b1254f3-8e1c-33a5-a5ef-d94da92bdb77 | -17.27396 | -46.03946 | 2026-08-30 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32fa5237-47a8-3829-a079-0667315015de | -11.79239 | -51.05785 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 23e86e8a-5811-3929-859a-3cbe6343287c | -14.76675 | -48.73525 | 2026-08-30 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README46.md)
