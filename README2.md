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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82500326-4a7c-359c-bfc6-817b34bb95ab | -3.4763 | -50.0673 | 2025-10-23 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| b8f58611-2b0f-3efa-9a3e-7f903b4f1c2b | -21.6755 | -49.05861 | 2025-10-23 00:50:00 | TERRA_M-M | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 93b0be93-571b-31bd-8f88-47d78244ded4 | -23.08395 | -50.15217 | 2025-10-23 00:50:00 | TERRA_M-M | BARRA DO JACARÉ | PARANÁ | Brasil | 4102703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| 9f3cbf1f-39ff-35ed-94c0-c769fdf1df4b | -20.97718 | -47.3628 | 2025-10-23 00:50:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 29.1 |
| f5cac070-7a20-3746-82f3-ab7b32e6e6b8 | -23.08254 | -50.14244 | 2025-10-23 00:50:00 | TERRA_M-M | BARRA DO JACARÉ | PARANÁ | Brasil | 4102703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 1fc5e882-6d69-330f-b406-e9e5407ec973 | -20.98442 | -47.36898 | 2025-10-23 00:50:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f6748fd4-7bac-32aa-a6ac-23c1c40fd410 | -22.18946 | -56.12372 | 2025-10-23 00:50:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 98c37940-bae7-310d-8d7a-139a75a5d535 | -22.6155 | -47.03815 | 2025-10-23 00:50:00 | TERRA_M-M | HOLAMBRA | SÃO PAULO | Brasil | 3519055 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0e1b7342-90ce-3ffc-95c3-220d0e25d9c4 | -22.19219 | -56.13253 | 2025-10-23 00:50:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fdbc6bf4-92b0-3a63-837e-dbed05bfa57d | -20.9821 | -47.35516 | 2025-10-23 00:50:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0eaa8447-e5f6-30a8-b993-a1fc40835422 | -23.07372 | -50.15022 | 2025-10-23 00:50:00 | TERRA_M-M | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| c20e9fce-1e4a-3952-8430-a7c4d8d60109 | -22.19054 | -56.11719 | 2025-10-23 00:50:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a507ecf2-13d7-3cb0-8e7f-b53f4ffdc14c | -21.02063 | -48.40892 | 2025-10-23 00:50:00 | TERRA_M-M | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| dda67fbd-e8cc-3580-b556-3881b4895c98 | -21.02248 | -48.4207 | 2025-10-23 00:50:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 11488552-d36b-3316-bcc6-93533dd01525 | -17.60773 | -46.59443 | 2025-10-23 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 99e9f63b-7e6f-3c08-b64f-2727585f1ec8 | -19.26876 | -51.97771 | 2025-10-23 00:50:00 | TERRA_M-M | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d34d230f-acbf-3ddf-bceb-7426aa697d6c | -18.6985 | -47.04985 | 2025-10-23 00:50:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 07c92213-a65b-32fd-9098-8f59103bbc83 | -18.13583 | -52.50754 | 2025-10-23 00:50:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| edfc5dc9-54a4-3b59-8c13-f8be49176015 | -17.55286 | -51.05 | 2025-10-23 00:50:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8af18766-3143-3878-a7b6-52263c9b1192 | -17.55148 | -51.04044 | 2025-10-23 00:50:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 34653ddf-51ee-3954-9ad0-3f8001150d25 | -17.61063 | -46.61185 | 2025-10-23 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9233dea0-c6f0-3dfe-846f-6638ab5ed95d | -17.39792 | -55.10142 | 2025-10-23 00:50:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| b0f299e3-73eb-3aa4-a339-4066c812a900 | -17.61651 | -46.60505 | 2025-10-23 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 78af1ce8-bb62-3c25-8c58-5a7daa660f59 | -17.39656 | -55.09037 | 2025-10-23 00:50:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| ea08e21a-31f2-31ef-b330-d283937e9cef | -17.649 | -46.65241 | 2025-10-23 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 32.5 |
| bf6f27e9-18f5-3b33-ab5c-79a07bf10396 | -16.48067 | -46.47523 | 2025-10-23 00:50:00 | TERRA_M-M | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 1edb97bd-8755-3315-97e6-88777ca91095 | -18.14594 | -52.51545 | 2025-10-23 00:50:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 899f6376-ff10-3a9c-8e9f-9b37466a9ad5 | -19.26856 | -49.36186 | 2025-10-23 00:50:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2beb7adf-c81b-3620-aebb-0b37ac9c580e | -18.22903 | -47.41513 | 2025-10-23 00:50:00 | TERRA_M-M | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 46.1 |
| f1d2b2b1-6bde-33f5-aced-8d371c122e69 | -18.2281 | -47.42185 | 2025-10-23 00:50:00 | TERRA_M-M | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 41.7 |
| a633c4c2-69f0-3460-bc4f-b4b8cd994ff9 | -17.39382 | -55.09657 | 2025-10-23 00:50:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 2c3b40ec-2c93-3762-8be2-15efeab7ff32 | -17.14935 | -53.30879 | 2025-10-23 00:50:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8f5badf7-541f-3763-9cad-bdf6fcb5dec6 | -19.26693 | -49.35101 | 2025-10-23 00:50:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 30.8 |
| f5922b7d-cc63-33fc-a00e-041583d9bf34 | -18.23152 | -47.42997 | 2025-10-23 00:50:00 | TERRA_M-M | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1a0e02dd-193c-36d7-a32b-49f872a8bd3f | -17.56047 | -51.03891 | 2025-10-23 00:50:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6ec60e3c-f211-3bc8-a3c7-7e87981a2162 | -18.22569 | -47.4069 | 2025-10-23 00:50:00 | TERRA_M-M | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 773af3e9-52f3-34c0-aab5-fb52d6b8fa41 | -19.1547 | -49.13242 | 2025-10-23 00:50:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 6e1b51d4-68e2-30ca-a745-7e66a53e43aa | -18.1371 | -52.5168 | 2025-10-23 00:50:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b99f912d-3f3f-3333-8d35-6b86f18de4da | -16.97294 | -51.88748 | 2025-10-23 00:50:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b2b51afe-d5b7-37c6-a9b9-72d831ecf7c8 | -11.07391 | -51.58049 | 2025-10-23 00:52:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e6c9fe73-d1a3-32bc-a8b0-b4709d43c816 | -15.58472 | -49.06935 | 2025-10-23 00:52:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cdd766eb-5d4a-3d7e-9a3d-90fe3d3db00c | -11.36317 | -49.80759 | 2025-10-23 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 074d1832-05b1-3f78-96c2-82d3bbb176d9 | -15.67337 | -53.35063 | 2025-10-23 00:52:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 15e386cc-6174-318f-90c7-f853a8476c03 | -12.38745 | -57.5242 | 2025-10-23 00:52:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 34e8ea4e-5a5e-357f-8de9-7732a8726384 | -14.69647 | -52.81271 | 2025-10-23 00:52:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7046d781-782c-3fd7-9ccd-c646e325b06a | -12.54975 | -52.2233 | 2025-10-23 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 10877ae3-8dc1-3bf1-8d91-c9211a43ddb2 | -10.65837 | -54.31964 | 2025-10-23 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| da15301d-4416-30a6-aab9-a05c96f74a14 | -14.84244 | -54.21709 | 2025-10-23 00:52:00 | TERRA_M-M | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c6c8257c-369c-3c09-9d2b-914936a29c7a | -12.78478 | -48.57033 | 2025-10-23 00:52:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 82d0863d-ffea-3965-bd71-c43838da7e5c | -16.54965 | -52.61865 | 2025-10-23 00:52:00 | TERRA_M-M | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9358dc7d-2c89-38e0-b067-ccef6371a9d0 | -13.79829 | -52.7713 | 2025-10-23 00:52:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 83c7931a-f9a5-3250-952e-49e8c576533d | -12.90013 | -48.4949 | 2025-10-23 00:52:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d617dd52-3288-3343-bf0e-8dcf988ed8f6 | -11.26717 | -54.18985 | 2025-10-23 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6df74b8-dcd4-386e-89a2-0f977109ce2a | -13.65106 | -48.64747 | 2025-10-23 00:52:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d66d6ea3-208d-3b1c-821f-02e33a2ef3a1 | -9.56043 | -47.77332 | 2025-10-23 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0fa020b1-0d86-3b80-85bc-264cb5e1c19b | -13.79956 | -52.78038 | 2025-10-23 00:52:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f6792e73-59f4-328a-ab60-504c02eabad8 | -11.35277 | -49.80927 | 2025-10-23 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 690f77d5-d27b-37b4-b252-bc09f5fce419 | -13.45806 | -48.82664 | 2025-10-23 00:52:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ae06da24-4abd-3d96-a076-473cd5d5dbc5 | -15.3599 | -50.55975 | 2025-10-23 00:52:00 | TERRA_M-M | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 37e6d9f7-2ed1-3151-894f-07b255c3fe39 | -13.12587 | -48.24935 | 2025-10-23 00:52:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ed8fb282-8027-3692-af47-d82c15b92b50 | -11.35929 | -49.78207 | 2025-10-23 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 5601a9d0-e90b-35a6-b80f-c1844e6044fe | -12.69164 | -48.63833 | 2025-10-23 00:52:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| cc7caef6-413a-3ea3-9faa-822aefffceb9 | -12.52196 | -48.58108 | 2025-10-23 00:52:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5ee8fec9-0d4e-3b73-9f01-9d80c778c56f | -12.00945 | -46.74536 | 2025-10-23 00:52:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 36c418a6-092a-3ae6-a83c-a2ae32723d9b | -12.12998 | -62.9749 | 2025-10-23 00:52:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 34.7 |
| cdeb921e-a8b2-345d-80e0-e5d5311ddac5 | -9.61392 | -46.8753 | 2025-10-23 00:52:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| df2bfb60-8ac0-3e68-b853-76cd65e6cd63 | -12.01201 | -46.75153 | 2025-10-23 00:52:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| bff14d6d-379a-3fae-b06b-5d77d98a956c | -13.78944 | -52.77262 | 2025-10-23 00:52:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 77bb66c3-2ac1-309a-8909-cc50c68f32fc | -15.67212 | -53.34143 | 2025-10-23 00:52:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7703556e-7c15-3c33-944e-33cefc1d5c75 | -12.25193 | -49.58953 | 2025-10-23 00:52:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1697f977-e181-328a-baa4-152b0b81f65c | -13.79072 | -52.78171 | 2025-10-23 00:52:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c290e8cd-f4fd-3018-82ce-7001ff30fd62 | -13.46291 | -48.83349 | 2025-10-23 00:52:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5f474177-2e08-3a30-90f9-fe836c35283d | -11.25076 | -49.88353 | 2025-10-23 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4aba3a87-fa58-3481-b075-d75ec3510000 | -10.52462 | -50.21997 | 2025-10-23 00:52:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 73833a16-71c9-3043-a1fd-a7a19c7384b6 | -11.07244 | -51.57038 | 2025-10-23 00:52:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 9835eec9-8397-3d56-b0da-9509e028564b | -12.82339 | -48.66448 | 2025-10-23 00:52:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b330b8ac-778c-3054-b80d-00b62933c48b | -14.84369 | -54.22653 | 2025-10-23 00:52:00 | TERRA_M-M | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 26.2 |
| e5955c00-1b75-318c-a038-c8f7430798e0 | -11.35082 | -49.79652 | 2025-10-23 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 5a6e09b3-988a-3d4b-ade6-4cf17f868b68 | -11.36124 | -49.79488 | 2025-10-23 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 08e6af61-127d-3de6-a355-1fac1a0348c7 | -12.70093 | -48.84381 | 2025-10-23 00:52:00 | TERRA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 88706bf4-c6b0-34dc-ad56-a59547fb470d | -12.68054 | -48.64009 | 2025-10-23 00:52:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 863d1a9b-69df-38b7-a240-44cf81755c57 | -16.08398 | -51.41165 | 2025-10-23 00:52:00 | TERRA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4daaedfd-b918-3724-a73e-55ab950f7440 | -11.24881 | -49.87089 | 2025-10-23 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f9e97719-bda6-3967-8513-75dfab4950c0 | -10.53122 | -50.19376 | 2025-10-23 00:52:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 7e1b3a4c-0bb4-3c0b-bd6c-3f49858a3778 | -3.15509 | -50.17073 | 2025-10-23 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c77fe88b-3647-3bdc-bf68-c87a426b0fcb | -3.03295 | -49.49183 | 2025-10-23 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 51c870d7-48c1-3de5-8f5c-bbc1a9359041 | -6.28542 | -47.00197 | 2025-10-23 00:54:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| cb9cc529-3a4d-3b73-b4fa-f20e854f94b4 | -7.27942 | -49.99804 | 2025-10-23 00:54:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 12953227-1159-3764-97d0-6644e97b04dd | -3.84686 | -51.67189 | 2025-10-23 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6d9562e9-c4fa-3d0a-ad6e-3f8a947ef761 | -6.28941 | -47.027 | 2025-10-23 00:54:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e822f24e-99ef-3d95-8228-fdedca060309 | -3.22247 | -49.35776 | 2025-10-23 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 1ccd189a-069a-3816-8157-c90e1da5d996 | -4.63879 | -49.54257 | 2025-10-23 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ec06d382-849f-35cd-a9d3-5cf68aa3838f | -3.67825 | -51.34007 | 2025-10-23 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3a3dda86-6ffa-33f2-b5a4-91119fab51c3 | -4.70702 | -48.12002 | 2025-10-23 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| ed492c35-7d66-3a72-81df-50d300d3d060 | -2.81668 | -54.38458 | 2025-10-23 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d7546e9d-4e2b-3136-aa96-e67a0f36c6c5 | -2.25696 | -51.92457 | 2025-10-23 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e910e8b9-783c-3bbd-8382-a1926edb0e2d | -6.09155 | -49.37243 | 2025-10-23 00:54:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2d4e0d2f-6603-35f1-8ffe-5335de1155f7 | -6.99959 | -46.99842 | 2025-10-23 00:54:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 4e1ea850-8d8f-302b-8c81-e7a063f1f1e3 | -4.1898 | -50.10597 | 2025-10-23 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| ba534f6d-a7c3-3523-b32d-7afce928069d | -7.27733 | -49.9838 | 2025-10-23 00:54:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |


[Clique aqui para ver as próximas entradas](README3.md)
