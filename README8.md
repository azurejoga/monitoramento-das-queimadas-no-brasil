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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39dcb8cb-d81e-3a30-9cf0-eaa55e0e878a | -12.73817 | -54.20033 | 2026-06-03 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51bc69d7-74d3-36e4-9838-dfc729c4fb73 | -11.57786 | -56.33311 | 2026-06-03 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c995ccd7-7190-3a67-8f6c-dee5c2609b5d | -9.88729 | -52.44191 | 2026-06-03 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c02039b-09fd-3b34-9f41-8dee21150e46 | -10.53824 | -46.62642 | 2026-06-03 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97027d59-7f9a-3664-9ec1-4a828faf74ae | -9.98328 | -51.02089 | 2026-06-03 05:01:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f71d823-c44f-3059-a7ac-9b25d49e9dcf | -11.26113 | -54.7261 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93d0bec2-3d95-3dbc-bdc5-c4a06ac74144 | -11.25631 | -48.35838 | 2026-06-03 05:01:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01100ae8-22c1-3919-a8d6-8a2871de94a1 | -11.81165 | -57.35599 | 2026-06-03 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb341567-e91f-3e64-b65e-c4dafe5094d8 | -11.56755 | -54.58289 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82515ed7-2c43-3ce4-8997-fd1e67987a4a | -10.86245 | -53.74445 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebce3f6d-fde6-30d8-9946-e34acbdb5118 | -11.62395 | -55.18368 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a092e48b-4bf1-3c9d-9b6a-d23f0f0866c9 | -12.73447 | -46.97073 | 2026-06-03 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 18f2170e-2996-36d9-9bc4-0d06137fd933 | -12.08525 | -48.41781 | 2026-06-03 05:01:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea05d28b-be19-3728-a415-d5d12e059083 | -11.26385 | -53.96468 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbf4a981-c4c8-3377-8bb6-21dc2f60fd0b | -7.50404 | -55.00129 | 2026-06-03 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dc67f2c-4e35-3204-8fb1-fda90149135f | -11.26995 | -53.96928 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| accea017-9411-3268-b30d-0c0463288723 | -11.75742 | -47.07074 | 2026-06-03 05:01:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ea94720-7f1e-3504-b614-81de9c39cbd7 | -11.88587 | -57.83674 | 2026-06-03 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4ac8a2a-bb55-38a3-84ab-8423017afda9 | -11.63186 | -55.17757 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d97047d-470e-3cc8-8b06-73fc679d46ee | -10.90232 | -54.13335 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f628f387-6035-374e-9f9f-5f1b587b5e93 | -10.54038 | -46.63019 | 2026-06-03 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 033d9d26-31d4-3105-9f27-728e2d6fa2da | -9.88785 | -52.4383 | 2026-06-03 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4aec3bd4-b26f-3eb1-8466-c552fb553b2a | -11.75357 | -47.07349 | 2026-06-03 05:01:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8475fd66-4471-35f0-9920-7f45a8654342 | -10.5977 | -53.47456 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4940d11a-ffde-3f20-8be4-6ea8b37a302f | -6.99156 | -42.87769 | 2026-06-03 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 85f5f0b6-6717-3a2f-b486-7aa4d7535059 | -12.72649 | -54.20932 | 2026-06-03 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80bee898-3aea-3429-8be8-dd88394aecca | -11.13933 | -45.14398 | 2026-06-03 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90322539-e686-3dcd-a855-0cadcf886120 | -10.86578 | -53.74499 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8670eb50-ecd6-3213-b34f-48f6b1cd8d05 | -12.73315 | -54.21041 | 2026-06-03 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87ae2b5d-80a9-3756-ac9c-3dc460510f0b | -10.81906 | -56.59309 | 2026-06-03 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10751c04-4692-34d8-af80-a796b6408ead | -11.57372 | -56.3364 | 2026-06-03 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38fffe91-7afe-3df3-b409-5f1f43827af3 | -12.73873 | -54.19679 | 2026-06-03 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93b7017d-d89c-38b1-9435-aa5021f2446a | -10.54104 | -46.62547 | 2026-06-03 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07a397cc-bb8c-35d1-9e4b-f692bde3e79b | -10.46256 | -51.92099 | 2026-06-03 05:01:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f6e4def-e8f4-3315-aae7-078ad996d7fb | -10.87355 | -53.73903 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1eed526f-7243-34b2-9492-37b60cbb170e | -8.57733 | -46.00155 | 2026-06-03 05:01:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d969fd0-8df8-3aff-8d83-19f46467c8de | -10.81484 | -56.59651 | 2026-06-03 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 909f8f67-aaa4-3054-8f0a-dd94f67b45d4 | -11.56974 | -54.59055 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d4f7000-1579-3b86-86fe-2edfac3018e5 | -10.87409 | -53.77881 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7106dcdf-edeb-33f2-a150-82f5dd270148 | -11.62454 | -55.18006 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a9e1a1e-12dc-3021-8afe-29165a7cfafd | -11.20842 | -54.98934 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f5fb4d1-2670-3fe1-a865-89ee7b0edfb4 | -11.47684 | -57.10575 | 2026-06-03 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f389466-b829-3ec6-9343-da4dfd67aea2 | -10.85968 | -53.74039 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 389e568d-b56e-358b-934d-10f0ada64981 | -10.87022 | -53.73849 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dffc497-1195-3ac2-804b-babfbf8290ae | -11.56812 | -54.57934 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9b49251-1c30-30ec-9793-ad782a05366b | -10.54759 | -46.62755 | 2026-06-03 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7deeb990-6f18-3749-9016-0e36e4a91242 | -11.12628 | -45.12222 | 2026-06-03 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 67f76fae-508b-36fc-afc4-d9a66777f622 | -11.75751 | -47.07897 | 2026-06-03 05:01:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 847502a4-3016-3f09-984e-7b343e8024f7 | -11.62059 | -55.18311 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc21d3d3-6826-300a-88f6-1fcb00c076ea | -7.95378 | -46.84467 | 2026-06-03 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75b504c3-ec8c-3098-b786-ea957305b7a5 | -11.88137 | -57.84057 | 2026-06-03 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82cc873a-8963-32d4-a5dd-4cad2bc70971 | -12.17208 | -54.54356 | 2026-06-03 05:01:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65f7a4bc-3829-3530-a0f5-373a7547e27e | -11.62849 | -55.177 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2c9141e-6579-3958-82e7-ab42f9ec9d53 | -11.57088 | -54.58344 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4c64bd8-8d68-3884-9ced-a5db927a56a5 | -11.99467 | -45.1515 | 2026-06-03 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d79b5df-3a74-31e9-a9cd-fdbaa0f93bc3 | -11.25686 | -48.35456 | 2026-06-03 05:01:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d0fc001-a485-3029-af93-ef61ba1de10b | -11.62674 | -55.18786 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9bf51238-8f54-39a9-924b-0d03698d1fa3 | -11.7568 | -47.07554 | 2026-06-03 05:01:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1a052cda-0b04-362a-bcf4-0abbc8648b73 | -6.99281 | -42.87579 | 2026-06-03 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3c54949e-e33f-3f4b-a9a2-e7e465c76e0c | -11.8154 | -57.355 | 2026-06-03 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00285311-1be7-31e2-ad7c-9277848e9974 | -11.75618 | -47.08033 | 2026-06-03 05:01:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7524b03c-4856-3e85-b1a5-e214f5fa206c | -10.26056 | -52.08057 | 2026-06-03 05:01:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59d7abe8-5a7e-3a9b-acd9-9d98470d6704 | -9.18569 | -58.05511 | 2026-06-03 05:01:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0d25a8b-96e5-3cf4-91f5-a74e51e26e0a | -11.56535 | -54.57523 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96d99cf2-c5b0-3160-b4c6-3b6cbc4c9af4 | -8.08536 | -49.08871 | 2026-06-03 05:01:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 600f9161-911a-3276-9763-a2e7e2bde556 | -11.62791 | -55.18062 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e3e92eb-1503-3f8e-a792-7fbe01b340f3 | -9.76836 | -55.74511 | 2026-06-03 05:01:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac669a61-f950-39b4-8b34-c4112f9712a8 | -11.25718 | -48.35727 | 2026-06-03 05:01:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5cbf8085-9906-32d0-afd6-0e065dc6165a | -10.85468 | -53.7504 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f6b572b-a64c-3f7b-ac74-ac1563c5e405 | -9.18092 | -58.05941 | 2026-06-03 05:01:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 53c6ad70-98b3-31bf-a24d-a9ae4310d528 | -8.8699 | -50.1904 | 2026-06-03 05:01:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6327b72-54c4-3263-8e76-8683fc5eacbb | -11.63127 | -55.18118 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aafa1995-a7c9-347c-b927-208f429a0ac2 | -11.62732 | -55.18424 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a5c5b27-b729-3bc9-b29d-10a8d165e046 | -11.32352 | -51.39222 | 2026-06-03 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d825599-e0d6-30ca-bb02-090b675aec25 | -10.98043 | -45.09599 | 2026-06-03 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c86b136-2a17-3470-8b1e-37dcfe6bdfc4 | -10.5357 | -46.62967 | 2026-06-03 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9734288-7aad-3c9f-ab06-2168e3739007 | -19.16846 | -55.1839 | 2026-06-03 05:04:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 1f7b0922-31c7-325d-801b-4487bcac1b29 | -15.45572 | -55.83558 | 2026-06-03 05:04:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed6be40e-0660-3776-85f2-c995b31442ba | -14.08277 | -59.38292 | 2026-06-03 05:04:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bba7472b-e45f-31d4-a716-eb1f73122c51 | -19.16512 | -55.18333 | 2026-06-03 05:04:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 99188d8e-7703-391e-a86e-74979ce9ffc4 | -17.44514 | -42.62725 | 2026-06-03 05:04:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 313ac0fc-85ed-30a8-858a-0ea0adef6af0 | -16.90888 | -51.85365 | 2026-06-03 05:04:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7732529-9457-3ea7-a5f3-f0698d8d1908 | -16.14628 | -58.49253 | 2026-06-03 05:04:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1295cfce-ad6e-3f33-81ea-2abfd150b463 | -16.58241 | -45.88066 | 2026-06-03 05:04:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7cdf718f-50c0-3325-b4a4-2792f6512ddc | -16.59787 | -58.23701 | 2026-06-03 05:04:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 77d80041-50f7-309b-9fd0-533d212b2acf | -14.08368 | -59.37784 | 2026-06-03 05:04:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6df0d5f8-a6ea-33ba-b50f-8825cb37e7a2 | -13.66322 | -55.03837 | 2026-06-03 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b120675d-6eaa-3d9a-a6ae-b10f9fc466f5 | -16.58281 | -45.87725 | 2026-06-03 05:04:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| df2a3540-5a41-39c9-91ad-c228ca1589e0 | -18.37696 | -55.72292 | 2026-06-03 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 7a114f49-2a4c-343b-8b59-8f5ad98e5a25 | -16.14187 | -58.49621 | 2026-06-03 05:04:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1a1fedf3-b1da-344f-b1a2-b6680a0430b6 | -16.14993 | -58.49321 | 2026-06-03 05:04:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ac96da61-431d-3e42-b965-605f95ad2b1b | -16.14552 | -58.49689 | 2026-06-03 05:04:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| cc4f3a50-284e-3138-9fdd-d156801e615b | -18.62015 | -49.19381 | 2026-06-03 05:04:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fbf131ba-91c4-3d2a-942e-d663e7e02c56 | -16.57988 | -45.87968 | 2026-06-03 05:04:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f4f1a95-5d99-34c4-80db-0f10497e37b5 | -17.52768 | -53.69152 | 2026-06-03 05:04:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 693506fb-3751-3cfd-92fc-e61085f0b73b | -17.93703 | -52.2221 | 2026-06-03 05:04:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11009649-ea90-3f1d-9abb-68e724858ea9 | -18.46476 | -54.7068 | 2026-06-03 05:04:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4cdd9f5-3cd3-31e6-9b43-1b2c41487eef | -16.58521 | -45.88039 | 2026-06-03 05:04:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 10201231-982f-30fa-8828-c60f6d5f3e31 | -20.88667 | -48.98698 | 2026-06-03 05:04:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 58b4f977-f888-3fce-ac82-41f492728aa2 | -12.80781 | -54.86381 | 2026-06-03 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README9.md)
