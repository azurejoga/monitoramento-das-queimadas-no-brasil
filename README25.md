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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 879ce32e-dc5d-3112-bf37-13d106b06bac | -25.23034 | -49.62896 | 2025-07-17 04:51:00 | NOAA-21 | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b02e323d-c547-3c81-8a9f-22b21aa0c2f4 | -21.64644 | -53.15117 | 2025-07-17 04:51:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75e66354-3268-355e-9735-86bcba0c6834 | -19.45956 | -55.44222 | 2025-07-17 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f3e6ac89-2796-3c6d-bf29-11eb76cebe76 | -18.58708 | -51.81294 | 2025-07-17 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8885fe4-f6df-365e-801e-8687bc7e8395 | -18.83918 | -47.68402 | 2025-07-17 04:51:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8069751-0859-337c-8e43-5eb8465accb1 | -20.91356 | -55.75259 | 2025-07-17 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f403c92-e601-38d8-bea2-80ccaed94296 | -20.1847 | -48.72729 | 2025-07-17 04:51:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 230e6b88-cbed-3243-bf28-ef6576a0bb2e | -20.43151 | -46.59429 | 2025-07-17 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb522732-5406-311d-874e-a6ad0269dab8 | -19.44613 | -48.5419 | 2025-07-17 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc8adf69-9ddb-323e-bfa9-d75a852bbdac | -19.23605 | -48.93192 | 2025-07-17 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43a4c0ce-7d63-361e-871b-c1b54630fc91 | -19.96093 | -48.99246 | 2025-07-17 04:51:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c883ce74-c413-3499-afe9-294aef6e8b62 | -20.96813 | -55.95786 | 2025-07-17 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6fc356ec-4d5b-3005-aa1b-59b95d911d7b | -19.5411 | -49.66993 | 2025-07-17 04:51:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 99ec983e-1025-37ae-9cb9-5dc2e2eb84a4 | -25.12121 | -49.18567 | 2025-07-17 04:51:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b650f1bc-2732-3434-9149-d5b2c331fd6d | -19.5443 | -49.67554 | 2025-07-17 04:51:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7b7fb210-97d9-300b-99b3-69ecf224ebd7 | -19.47373 | -55.45212 | 2025-07-17 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| cdaf4279-2225-3bca-b68f-69223dff2e31 | -19.4466 | -48.53815 | 2025-07-17 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a2b4f030-144a-3314-b371-9019028ea302 | -23.5219 | -47.01665 | 2025-07-17 04:51:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ea09209b-40dd-302b-a631-0269fb4a61b1 | -19.9614 | -48.98874 | 2025-07-17 04:51:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a3e5d0f5-4d56-3603-85f0-1824a75c2d27 | -23.79977 | -53.33478 | 2025-07-17 04:51:00 | NOAA-21 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b4c2fa14-8b22-34a8-8637-f3a92cc10280 | -19.4623 | -55.44657 | 2025-07-17 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5fa3455b-549c-3ef4-9203-a96f91e1811f | -19.31389 | -55.15985 | 2025-07-17 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f2e8f6a-b429-3908-8aa2-b3bc6db17efa | -20.98995 | -49.77308 | 2025-07-17 04:51:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| fcc29ba8-2615-3669-b74b-fac9cca00f74 | -20.11333 | -49.09956 | 2025-07-17 04:51:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be9e0ef3-4f48-3456-ba1d-3a0d8cce450f | -23.36362 | -47.27423 | 2025-07-17 04:51:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f102fdea-6af9-3522-a22a-d333f5e5a97c | -22.72713 | -47.61121 | 2025-07-17 04:51:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ec19f4d8-92b3-36ad-9ea9-fdefd49e1b65 | -19.54044 | -49.67496 | 2025-07-17 04:51:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 99cd8024-8b2d-356c-8d4f-41f2517bb09c | -19.47174 | -55.45213 | 2025-07-17 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 2cb5d2a5-4b44-37f1-8d48-f59d3edd1d56 | -23.06393 | -51.51706 | 2025-07-17 04:51:00 | NOAA-21 | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 07d8bad0-bcc2-3ff3-add6-b7c3523470d3 | -19.96045 | -48.99617 | 2025-07-17 04:51:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44bc030a-729c-3684-ae3f-acc48bc944aa | -21.08064 | -48.6868 | 2025-07-17 04:51:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 69d818dc-85d6-3d17-95a2-fa38f8e4735f | -23.80034 | -53.33083 | 2025-07-17 04:51:00 | NOAA-21 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 90d1ba62-14d1-34b0-bf06-c181fa61ba48 | -23.27965 | -47.70552 | 2025-07-17 04:51:00 | NOAA-21 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f788e0d9-c108-3552-9027-b725f62e59fc | -23.23092 | -46.40293 | 2025-07-17 04:51:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c986a62d-f9d2-358e-96bd-abdb09e10d1f | -18.97983 | -48.30906 | 2025-07-17 04:51:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87034e98-4deb-359a-b6bc-c27c311f6854 | -19.96498 | -48.99305 | 2025-07-17 04:51:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0b0203ef-c860-33e4-a7e2-303e812fbea0 | -19.47883 | -49.29271 | 2025-07-17 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 538022c3-6288-3a75-8017-76e04eb17e4a | -23.52113 | -47.0166 | 2025-07-17 04:51:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| af26b518-ac9f-3da2-a07a-9b2308fc5498 | -22.39549 | -49.79353 | 2025-07-17 04:51:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 0d61512f-27af-36a6-831e-3ee1c3bf6fcf | -22.24331 | -49.61333 | 2025-07-17 04:51:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 50e0d916-5db6-389d-85a5-fcf382687ae5 | -18.65649 | -55.73132 | 2025-07-17 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e4535514-42ab-3b46-a540-e7bae53702f1 | -18.59111 | -51.80951 | 2025-07-17 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 61d5adb7-7415-3d16-bb00-2d5cbe16db73 | -22.66008 | -53.37816 | 2025-07-17 04:51:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4dee454d-29fa-367f-b573-108c9e7cbc96 | -18.65373 | -55.72689 | 2025-07-17 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 952282c4-2d96-3df4-840a-d9ab369b2fe4 | -20.99062 | -49.76781 | 2025-07-17 04:51:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| 7ef70a1b-457e-3794-a5a9-0e4e104297c8 | -23.51706 | -47.01619 | 2025-07-17 04:51:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 44b0b6a0-a4cf-3b6f-a9fa-60c01b2b2d6c | -21.1839 | -53.17945 | 2025-07-17 04:51:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f891c50-dfe7-31a9-b113-02214a9071d1 | -18.84085 | -47.68177 | 2025-07-17 04:51:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c94dc53-f6b3-3680-ae53-7a96d39605c5 | -20.99387 | -49.77365 | 2025-07-17 04:51:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 5151d1c3-7f08-3157-a742-e94c9ed46dbb | -22.29964 | -49.12286 | 2025-07-17 04:51:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f967f39d-0867-38d7-a91d-1d7d7ba8b065 | -22.87546 | -46.79667 | 2025-07-17 04:51:00 | NOAA-21 | MORUNGABA | SÃO PAULO | Brasil | 3532009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3594fc05-7b25-3d01-b532-e0de7fe476cd | -21.08386 | -48.68908 | 2025-07-17 04:51:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d75fab6a-5d6b-3302-a6c2-6db388ba6f9f | -19.53657 | -49.67438 | 2025-07-17 04:51:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e6b163c9-8ac3-3274-804c-67cd94901221 | -18.42329 | -53.03196 | 2025-07-17 04:51:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd276c49-6884-3a5c-a72d-aa4e93b4903c | -19.45076 | -48.53862 | 2025-07-17 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f6ed5d6-54ee-392b-9139-29ad91773a9d | -19.31449 | -55.15615 | 2025-07-17 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c159565b-a528-3ba0-aa1e-7c203c3aef5a | -20.99454 | -49.76837 | 2025-07-17 04:51:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| c6c80e5d-f840-39fc-8be2-10ea03b6fed2 | -23.25838 | -45.58116 | 2025-07-17 04:51:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 16034ef5-2697-3cb9-8d62-7f9381a8a1b8 | -18.6531 | -55.73071 | 2025-07-17 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 694731b9-5c42-3c45-82ee-c8ebd77cb4b0 | -20.9169 | -55.7532 | 2025-07-17 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24376b86-451c-3de9-a71b-a31b21a6b58e | -23.02377 | -52.64731 | 2025-07-17 04:51:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 9624ebf4-8724-39c7-81b9-f0705cbc8aec | -25.11693 | -49.18501 | 2025-07-17 04:51:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ee3e09b1-1379-3736-bef7-18be90c3417b | -23.25307 | -45.58091 | 2025-07-17 04:51:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b92d4ed6-6140-3fa8-a8ca-e770e0442a3b | -19.45028 | -48.54237 | 2025-07-17 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d48d3b0-da81-3923-a406-6beacd300661 | -23.08526 | -49.73405 | 2025-07-17 04:51:00 | NOAA-21 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 05f0ee88-6cc7-3d1c-9773-a41e48ca301d | -21.08436 | -48.68501 | 2025-07-17 04:51:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 332a317e-a7ca-364f-b65b-d189ddb36e3f | -18.59053 | -51.81347 | 2025-07-17 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b56a996f-d374-3220-9c21-ca849d31b954 | -23.25872 | -45.57737 | 2025-07-17 04:51:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f65dd1ce-f7dc-3e82-933e-f124d0fbfe4e | -23.06027 | -51.51651 | 2025-07-17 04:51:00 | NOAA-21 | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 118ce7e2-d0d1-30d1-89c1-956326927f74 | -20.00791 | -49.04807 | 2025-07-17 04:51:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c63d09df-d05b-3f92-b887-3ea2d2fcbda5 | -23.61612 | -50.77638 | 2025-07-17 04:51:00 | NOAA-21 | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1e851e70-b968-3ef1-b956-bd11e9dec7ed | -21.08483 | -48.68742 | 2025-07-17 04:51:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ea2994a2-154a-3531-996c-f6a74d6929cd | -20.01242 | -49.04494 | 2025-07-17 04:51:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 22bd4df7-ed2d-350f-9900-c1c2e4c04cfa | -25.1174 | -49.18072 | 2025-07-17 04:51:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 41e3dee3-e3aa-34bc-85f6-01a5c7dc4edd | -28.76145 | -50.15071 | 2025-07-17 04:53:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0cbf67c7-3c5f-364b-a3ba-fc0ca1e62987 | -26.83479 | -52.89218 | 2025-07-17 04:53:00 | NOAA-21 | ÁGUAS FRIAS | SANTA CATARINA | Brasil | 4200556 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a9cca8c9-37cc-306c-8655-18d5c45b62da | -26.83538 | -52.88768 | 2025-07-17 04:53:00 | NOAA-21 | ÁGUAS FRIAS | SANTA CATARINA | Brasil | 4200556 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 331c83dd-eaa6-3e59-a337-7ef5de49a1bd | -28.89583 | -50.13551 | 2025-07-17 04:53:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0183ff9d-ad7f-3e74-8d00-daf9bcf16150 | -27.07938 | -49.42804 | 2025-07-17 04:53:00 | NOAA-21 | APIÚNA | SANTA CATARINA | Brasil | 4201257 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7c9cb56d-9e1e-30c7-a917-8d8b657f3cdb | -27.20875 | -50.6639 | 2025-07-17 04:53:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 60ee1c0b-2de7-33a8-bc29-65ff4d93504e | -25.97966 | -52.3398 | 2025-07-17 04:53:00 | NOAA-21 | MANGUEIRINHA | PARANÁ | Brasil | 4114401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 569cf098-2466-37e9-ade0-3e28eac936d2 | -20.0216 | -49.0507 | 2025-07-17 05:00:00 | GOES-19 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 5a92b025-43df-35e5-83d7-70d0ecd7f5d3 | -5.6754 | -43.7147 | 2025-07-17 05:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 1f9a06ac-76a2-353e-a3ac-a59b66f3f642 | -20.0013 | -49.0551 | 2025-07-17 05:00:00 | GOES-19 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 56.9 |
| e2ef55c8-24ee-3ba8-8323-abbe4dad3390 | -17.3628 | -44.1399 | 2025-07-17 05:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1320927c-5ff7-3efc-9095-f5ab18be84b5 | -5.6567 | -43.7161 | 2025-07-17 05:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 146.8 |
| f15ec081-c304-3505-8b55-dcae44681ad4 | -3.3772 | -47.4792 | 2025-07-17 05:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 294c2dcd-3334-3720-b20e-38fb43ded648 | -6.7194 | -44.3231 | 2025-07-17 05:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| bc5d314f-9c0d-3c28-a421-c782c4c07022 | -3.3958 | -47.4785 | 2025-07-17 05:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 6bab04ee-d096-358e-9307-edba3a081583 | -6.7194 | -44.3231 | 2025-07-17 05:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 381bf69d-c560-3298-abb7-474b52c69aba | -19.9623 | -48.9949 | 2025-07-17 05:10:00 | GOES-19 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 96.3 |
| f5ca218b-60cd-3108-b3eb-603a283d254a | -5.6567 | -43.7161 | 2025-07-17 05:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| adcf363f-4d7e-37e4-8ee5-39e7ebaccd1e | -5.6754 | -43.7147 | 2025-07-17 05:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| ee3f6a7c-e1ec-3f82-ae51-d3f1d34635bc | -3.3772 | -47.4792 | 2025-07-17 05:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a9fcb413-4490-3a8c-81e9-8767110ce20c | -17.3628 | -44.1399 | 2025-07-17 05:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 0735d6bf-d09c-37e3-bb24-1eeb97d39ce8 | -3.0376 | -47.86291 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 385bb5d5-8ee0-3fbd-a084-30d4cb30506c | -3.04556 | -49.43037 | 2025-07-17 05:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 914a7e75-6589-3a4b-9568-6de1ef968c08 | -2.44353 | -47.32856 | 2025-07-17 05:10:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8ae7e45-f13d-357c-a748-88600b94e351 | 0.7672 | -60.49482 | 2025-07-17 05:10:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f72a6091-e5a1-337e-ad16-ad44d4ccc6fc | -2.44303 | -47.3319 | 2025-07-17 05:10:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README26.md)
