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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6264407f-e098-35ac-bb09-b78aaf16ce0e | -11.34163 | -51.12347 | 2026-08-18 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12441f13-c30d-38bb-9eae-9091f8262da5 | -14.30834 | -53.04241 | 2026-08-18 04:40:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93fdf058-73cc-3c70-86ff-60cc40fd1ef7 | -14.28377 | -51.93313 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e1eaf3f-f8ec-3878-a25e-80d3b9a92586 | -10.27715 | -50.44191 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ffaa739-b68f-3773-acaf-05402e1db8d7 | -12.52699 | -47.8932 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f85e2b90-5644-3f71-bd8a-44ea6dbcc7fe | -14.16913 | -52.91848 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9da122fd-908d-3d52-a663-b63ecc879413 | -11.36256 | -46.383 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7e5b9e34-2d11-39f1-953f-64b2bffa175e | -11.36627 | -55.42005 | 2026-08-18 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 956730a3-dd52-35f9-a89c-7707310aefae | -14.18783 | -52.92725 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 330bd649-bd9c-3005-bc90-9ea9ac137a14 | -11.14115 | -49.04328 | 2026-08-18 04:40:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b6579c5-4129-317d-aae4-88b65d4f490b | -12.68221 | -48.51157 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2eacc818-2eb4-3284-bc76-1c420cea3772 | -11.3405 | -55.27367 | 2026-08-18 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9744f22-0863-357e-bb13-35a1fb56af28 | -14.25996 | -51.93805 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 723365d8-cfc6-32fd-a509-45634703d9f0 | -11.04689 | -49.9728 | 2026-08-18 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e493d31b-9ed8-3446-954e-260754589ff6 | -15.6475 | -54.80469 | 2026-08-18 04:40:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a32ad4fc-2cb7-33b7-82b8-2634cfbaf36e | -14.81067 | -46.63744 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e04e492-b877-3c63-8335-3fc9cb0869b5 | -15.29207 | -56.44494 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2aa98a42-06d2-33c3-9b50-8b4a27481ae5 | -11.35699 | -46.39687 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fb45cf3f-8cb6-3478-833f-662960670644 | -14.17444 | -52.8953 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 5fa7e3c5-08ce-344c-b9ef-f859f855b9a4 | -15.22884 | -57.65934 | 2026-08-18 04:40:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce058370-d5fa-37b7-af8a-d309421d115d | -14.03577 | -53.68137 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2f734850-00d4-3669-b062-8754e1405fbe | -12.52197 | -47.88515 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72bc18e6-26d0-37ba-b436-f082d05ff65e | -9.4245 | -60.4161 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4aaad06e-6651-3ad1-96c2-02b92705433c | -13.40913 | -57.05122 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 568b70db-d607-3253-85f4-e7bbdb4d69eb | -14.17774 | -52.92278 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 3ddb9c66-dddb-3324-ae48-8d34320eab54 | -14.16996 | -52.89172 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bca10c43-f24d-34ca-ad23-0da3f0e3625f | -9.42437 | -60.4524 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| de606586-5c4b-3fef-b27e-7c549907c97c | -11.33649 | -45.9151 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88e4a799-d34a-314c-a4c1-ed4f1b7efd49 | -11.12603 | -46.49259 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7d15511-e149-348a-869b-56267f8882cf | -13.25967 | -51.65015 | 2026-08-18 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62823804-1d40-3093-ae92-48ab6536f4d9 | -14.85551 | -46.64114 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e62be42-80f4-3dae-ac56-27a2f6018992 | -11.33876 | -45.92309 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 170e0242-ce3c-3341-993e-721407c4567c | -14.80841 | -46.65251 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 63fb15e7-ae8b-3b9a-8a9c-312367d37972 | -14.25043 | -51.92698 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c7d59f04-ad73-3c89-ac73-101760a25948 | -15.24837 | -56.48795 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5f8cd32-1053-3c93-b8bd-d26c8bea0c5b | -14.81408 | -46.63805 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ad1590c-73a0-37f8-a9fd-db25cc0e36fe | -14.82202 | -46.63167 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 3cdc066c-c68c-38da-bc82-7e6d09847aa5 | -11.46972 | -46.56912 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b1ab5cd-df96-38ef-af7a-a464f1c785ed | -11.14804 | -47.28653 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72ebf0a6-3bc0-3f44-b3db-98c7aa256f22 | -15.25321 | -56.48893 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d794696-b577-3237-9eb3-79786afd2089 | -17.97646 | -44.42872 | 2026-08-18 04:40:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d27de749-4950-3e8c-b190-a3170fa806f3 | -14.80784 | -46.65627 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c3eaf2e-66f0-3e59-bf28-fc9c8d07e231 | -11.10991 | -46.49784 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| affdfc46-e274-354f-a53c-990538a0c99b | -14.81219 | -48.78172 | 2026-08-18 04:40:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef65b206-dd89-3d7a-9ee7-39134e122bdf | -11.61937 | -46.7788 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 084b28c2-4431-3aac-adb4-3146d3038447 | -10.77824 | -50.32658 | 2026-08-18 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8f5f811-4dd5-36be-98c5-81e15ba1238b | -12.76314 | -48.43348 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f27d895-3822-331e-b1ac-1b4543ab8d51 | -13.4611 | -57.06178 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d31ba3c5-e808-3b56-95a6-476bb730561d | -15.39059 | -52.79183 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4c2b7ce-2fbe-34f9-a6fe-832edbbaecc3 | -11.3711 | -55.42107 | 2026-08-18 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| fea4e832-1616-319c-be36-6e2ccaeb42b7 | -14.16989 | -52.92131 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6192bdb6-547d-33ac-8012-146b8a3bf991 | -12.22911 | -47.03304 | 2026-08-18 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3663623b-b8d2-37f4-bc4c-55515951189b | -16.26952 | -49.29839 | 2026-08-18 04:40:00 | NPP-375D | DAMOLÂNDIA | GOIÁS | Brasil | 5206800 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 52109bc2-faf4-380e-a6f8-8b212a5fb20b | -11.53004 | -46.64457 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 13d854c7-1467-3df2-8099-869c92eacaa5 | -15.28722 | -56.44411 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89c719d2-a6d7-3580-b4bb-db8b1e9cfafb | -14.18205 | -52.93673 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 66303fff-a59c-36e5-8024-588f2c9f7efb | -13.93479 | -53.93128 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ccec825-908a-3fe9-9160-d79ace1ffcdf | -15.25806 | -56.48994 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdbb8b5a-846d-38e0-83b6-6f389b1c5dd5 | -14.43019 | -51.88907 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 564f5ce3-1e5d-3662-82e3-fcb8c3a242fd | -14.17882 | -52.90978 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 24.4 |
| d471084a-b020-3baa-be5d-072875d67707 | -11.32706 | -55.26569 | 2026-08-18 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4ff5545-7069-344d-8a8e-5c2faea3586b | -14.83281 | -46.65274 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7390b40-90a6-3760-ad0f-944b9881dd36 | -11.33933 | -45.91935 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7951a77-a0ce-3ca6-8353-49c530de536c | -9.42628 | -60.40606 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14136749-c148-3f6c-985a-f622e13a76ed | -12.25942 | -45.87635 | 2026-08-18 04:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95e2fbc5-d35a-38bd-9f9a-b5b145b744b3 | -9.16159 | -59.69791 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e102947-3340-34a9-b502-9b3d4b865aa6 | -13.93551 | -53.92736 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9a85bda-542a-3f65-a46e-681714899165 | -12.14221 | -48.26556 | 2026-08-18 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e53c6b9-8028-30fd-991e-defa67ce6788 | -14.97452 | -46.59356 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d693fe62-8362-3c6c-ab36-1160ba5f9cd4 | -9.42359 | -60.45593 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fdbe0f7b-ddc6-3644-8caa-b12a63fd3f74 | -17.9523 | -44.4302 | 2026-08-18 04:40:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78edbab0-4820-3c69-8115-862a57305737 | -10.27711 | -50.42033 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c747945b-bd64-3a28-aa47-0ba9bf00962a | -12.54089 | -47.84842 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c2e7d9d-aaf4-33f3-8eda-7c69d78269c9 | -11.12657 | -46.48905 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aedb404a-275f-3a83-9e2f-504b894b95c3 | -12.93843 | -56.6437 | 2026-08-18 04:40:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bd385de-cb6c-35d2-b8c9-e447193c7da8 | -14.46151 | -51.83961 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c5c7142-d729-3765-9a93-b5e60ee14cce | -14.82483 | -46.63622 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c4c15801-1b5d-3f42-809b-f84d980fa034 | -11.49038 | -45.1046 | 2026-08-18 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbc55d0b-cad9-31e0-baa4-bb6dae628e56 | -8.96031 | -60.53097 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1725f64c-6156-392d-bbaa-d6230ba515ee | -14.30215 | -47.18225 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88eb9aeb-cf80-382a-b4d6-f75eb2f4baeb | -15.22565 | -57.64831 | 2026-08-18 04:40:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b968f699-f237-3921-9e80-4236a2f2c3e2 | -14.0346 | -53.67318 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 07bf428f-3cf7-38c9-8b39-ed270299b0e9 | -14.03387 | -53.67711 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 21d418ec-cccd-319e-8667-47ea895a403d | -14.18596 | -52.93755 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 532c5324-5e7b-3725-ae37-7151a131dd6d | -12.2257 | -47.03937 | 2026-08-18 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d5433e3-e3f5-30a0-9961-c1a643525326 | -14.84869 | -46.64009 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4fb90c3-ce4f-34e6-a102-875938d5a102 | -14.03646 | -53.67746 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aef3f657-51a8-3f8c-8912-5cbd6861a055 | -10.27133 | -50.41072 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7ccb86b-d0b8-3685-87ef-6333930364c6 | -11.1 | -49.91305 | 2026-08-18 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8ff73287-e570-3201-ab2c-b1a81a382191 | -14.82941 | -46.62899 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b6bb798e-46dc-3484-8d1b-939b16fbdbbc | -14.23289 | -45.41127 | 2026-08-18 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a510eed-366d-3242-b1e7-778f91d932b6 | -14.81238 | -46.64931 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9500d8f7-57bf-386e-88f2-f668827ee3cc | -14.3055 | -47.20517 | 2026-08-18 04:40:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b8904c3-5c0c-3237-a18a-c9c2eea8c347 | -11.12646 | -47.27225 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 00751963-26f9-3765-9c9d-605511a5980e | -14.36197 | -51.87799 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ad406ac-63fa-3d2f-beb2-abb1e74fbf8b | -14.17293 | -52.9271 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| feda9122-136d-3a47-804a-254a31c31d2d | -14.30886 | -47.18333 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eac4a71f-d7d6-3e1b-b5ad-957c11ef7117 | -14.84927 | -46.63623 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 177325e9-ec1d-377f-833b-94bdbbc88754 | -11.13475 | -47.28437 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48bdd9a9-f6dd-3509-b5a4-92527b0a4d13 | -11.1425 | -47.27845 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README28.md)
