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
| cb78f0f8-74a9-3ba3-adbb-15df09ac2456 | -10.8744 | -49.55118 | 2025-06-04 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce3a5e50-e8a4-39ba-910f-306bd80daee7 | -11.90326 | -47.44615 | 2025-06-04 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcc70184-cc39-3977-8f1f-a4902d0b99d2 | -8.90805 | -50.04279 | 2025-06-04 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 883d61b1-7166-3f99-9502-0d6db9b44696 | -5.12319 | -56.11668 | 2025-06-04 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40631784-e317-3a7e-94bf-c43cfd03315b | -12.66871 | -58.2207 | 2025-06-04 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35761f26-b1f0-3095-842b-6f0fc638d2f8 | -14.01603 | -55.12527 | 2025-06-04 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6505f1f-fac1-33c6-80f3-bc3bfa2c403f | -11.90266 | -58.67753 | 2025-06-04 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94ffaa59-87c8-3db8-bf29-ede4e9254d5c | -11.90382 | -54.79299 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e600f52e-fc4f-345e-86a6-11cdb5d18869 | -11.91425 | -54.81292 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2079326-b151-3693-99e1-27907ddc9cc3 | -11.78769 | -54.77418 | 2025-06-04 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 234e4602-455f-39ad-8569-31c7095fa178 | -12.27843 | -64.27497 | 2025-06-04 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a0d5810-b59e-33ce-87de-1d9952212cc8 | -13.59076 | -54.28167 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a831346-939f-3ebd-8ed3-d75580b3d519 | -12.46326 | -54.91464 | 2025-06-04 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28c9150c-8145-3105-857a-a101e280c980 | -15.27131 | -51.47703 | 2025-06-04 04:53:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 45863853-0f08-3718-ac26-a35c4e652b0d | -11.90496 | -54.78588 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1f95696-d8a8-3738-853d-fd6a563aa52c | -14.72254 | -45.1022 | 2025-06-04 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 003e00f1-cde8-3feb-83be-b112c22b399c | -15.99724 | -49.71339 | 2025-06-04 04:53:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 002532f4-4e64-3aa6-8eec-bc364b79f29a | -11.89603 | -56.41168 | 2025-06-04 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0323fd9-bf59-34bf-acdf-5d0f313c4aca | -11.55323 | -56.42023 | 2025-06-04 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04b2f657-0724-368b-a5ba-958a6f4ce9d9 | -11.90616 | -58.68126 | 2025-06-04 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f45a476-5a67-3a6e-a113-4b194f2d3ac0 | -11.70644 | -54.557 | 2025-06-04 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57b0ec15-17b2-37af-bfeb-7276d545d903 | -11.90656 | -58.67826 | 2025-06-04 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8255666-e9d2-3491-b19d-9fd56ac94579 | -12.37033 | -54.16843 | 2025-06-04 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc424ef5-9398-390b-979c-54669a0beb8f | -16.18679 | -43.73034 | 2025-06-04 04:53:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8b4ea85-597d-3c2f-ad45-76b6430c07d2 | -11.89718 | -54.7919 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ece478a8-9474-3108-b0c7-9bfe9fab10ca | -11.917 | -54.81702 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6433bbf9-4d5d-33b1-8e64-b95ed8f28f3c | -13.14262 | -56.80414 | 2025-06-04 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de7bc24b-4a36-34fd-8518-85dacb742249 | -11.90702 | -58.67622 | 2025-06-04 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b545c8b-1b84-370f-b5bd-2d0e2c357c6d | -11.91644 | -54.82057 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ac1b886-1195-3b21-b4d1-ba958cdd8ba2 | -14.01659 | -55.12171 | 2025-06-04 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c023a3e9-346b-30c6-b276-5859b7450f17 | -11.91015 | -54.41019 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3dbde3b2-c46c-3679-aca8-e8cfc14ccfd3 | -12.52522 | -57.19151 | 2025-06-04 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 049f9db2-9ae6-34eb-a2de-32fd9db9c6dc | -15.27431 | -51.48184 | 2025-06-04 04:53:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c0949d3a-78b2-3d34-a031-69dd12c20c34 | -11.9005 | -54.79244 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9a2dd0f5-56db-3651-8c21-74aefaf35e68 | -14.71714 | -45.10168 | 2025-06-04 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c82a551a-acb2-3f49-8960-c993e0aa7a3d | -14.71794 | -45.09481 | 2025-06-04 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d505665c-5be2-3013-9ebf-66144b66c314 | -14.02763 | -55.13808 | 2025-06-04 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6dfaae0-9e35-332f-b25c-f83d4b723f06 | -14.71293 | -45.09087 | 2025-06-04 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 324612b5-11ba-3e06-a006-9130dd3dd561 | -11.64826 | -55.36746 | 2025-06-04 04:53:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79d7253e-cccf-3634-ade6-a15f04ab8759 | -11.56021 | -56.42141 | 2025-06-04 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c6c139d-5ab1-39b5-9d40-852d3c22e25c | -11.91814 | -54.80991 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| daf4f70f-8744-38aa-827f-fadc036bb69e | -12.37088 | -54.16492 | 2025-06-04 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f4d6fb3-1d91-3a99-a515-610f9653397a | -11.54777 | -56.43149 | 2025-06-04 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7c5b392-ea70-3055-992e-584fa99976cb | -13.09628 | -52.02453 | 2025-06-04 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 386c206a-20c6-3761-a655-e65ae6b6d359 | -14.01991 | -55.12226 | 2025-06-04 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2d14534-c1f7-399a-bb92-69eb75d5050a | -14.81366 | -48.45616 | 2025-06-04 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e95db836-e992-3ee8-a434-cf3acb951a15 | -17.68792 | -46.80912 | 2025-06-04 04:53:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8453d0f9-fc05-318a-be05-4653b1095f27 | -14.03208 | -55.13151 | 2025-06-04 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9444684f-8327-3b97-a436-26309020c476 | -14.68003 | -52.68718 | 2025-06-04 04:53:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71d15bd1-de18-3b2f-9ff1-074389db2788 | -12.29229 | -50.11071 | 2025-06-04 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a6f0a73-e7a5-3559-bc13-07004b553cc8 | -12.64969 | -54.12066 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 311abc6d-8b9a-3cf9-a8f0-365fc648c500 | -12.51519 | -57.18551 | 2025-06-04 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 520d6d21-319d-3b7f-b35b-18af76e6312c | -13.96353 | -56.77881 | 2025-06-04 04:53:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36671438-15f2-3890-9438-bdcccd314891 | -13.42963 | -47.53732 | 2025-06-04 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54c763e6-7ecd-3915-ae4e-1c00b3c01e6f | -15.2707 | -51.48131 | 2025-06-04 04:53:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d19ab9e-4263-369f-9e25-40e328067d4d | -12.51162 | -57.18489 | 2025-06-04 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e039eb25-6c84-3dbe-89c4-33ec37657ed4 | -14.33443 | -54.13836 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25b9908d-611c-324b-8100-a4985b017a9d | -11.90827 | -54.78643 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f688a9a3-574e-3c22-8fd3-708cdf9fa7f7 | -14.71174 | -45.10117 | 2025-06-04 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bcfe935-c00f-337a-8221-157beeffcef9 | -14.33113 | -54.13783 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9d66fd1-0b06-369c-a8ec-b044d50a42b0 | -14.71673 | -45.10518 | 2025-06-04 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad6b55e8-340f-3a0d-899f-c0b0a29f863f | -15.3292 | -51.25066 | 2025-06-04 04:53:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 689122e7-fcaa-3101-8383-e44ef72b942a | -12.45994 | -54.9141 | 2025-06-04 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db0e7f1b-3ada-39f5-85df-924cd0bc698c | -16.39951 | -58.18236 | 2025-06-04 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ac3fb34f-dfec-3ee6-a310-eb2ddf5a1817 | -12.28065 | -50.1025 | 2025-06-04 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e3ac23e-67ba-3750-aac6-469323b4d6d3 | -12.64583 | -54.08043 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d062fd5a-0e96-3126-92c3-6e841fff1e7c | -14.01934 | -55.12582 | 2025-06-04 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba0f4c75-f6e1-39e5-a1eb-8d32aeaf02e1 | -14.03426 | -55.13918 | 2025-06-04 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3150fa95-fc19-378b-bd20-542d680ab712 | -15.57134 | -47.85509 | 2025-06-04 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 440aa7a1-a93c-3fc1-8d26-c6f554958c8e | -11.64069 | -58.01809 | 2025-06-04 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63290ffa-db24-363c-ab6c-758a1bda12c9 | -14.71754 | -45.09823 | 2025-06-04 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1fa6bd02-7aa4-3a55-b9a2-1baa345ed08b | -11.80171 | -57.3552 | 2025-06-04 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d4a2615c-fb4e-3595-ad58-5945fee6682f | -13.14545 | -56.80871 | 2025-06-04 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 107cfc8e-9b6e-3e9a-9cf4-a32ce257bb90 | -16.40025 | -58.17808 | 2025-06-04 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2441e4fa-8c4f-3ced-8a71-d0dddc829e4b | -14.0241 | -54.47238 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b52b395e-d5de-3c09-a566-c64015f2d6c8 | -13.09973 | -52.02505 | 2025-06-04 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7ded700c-de49-3f04-a418-3970635fa0ca | -14.03596 | -55.1285 | 2025-06-04 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29a702ba-3c81-3ee4-90fd-4b569c4ab221 | -13.91609 | -54.66065 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cd68b22-55c7-3391-b1f7-4ee1e5bf4b34 | -12.08478 | -54.57623 | 2025-06-04 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b05d1ba7-5bbd-3575-baff-50396e0f7638 | -11.92146 | -54.81045 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3bffc40-e7cb-3b01-ad3e-867390d2167a | -14.71214 | -45.0977 | 2025-06-04 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de5a7eb9-2a72-32f7-9c86-75b6d1d4bd6b | -11.65221 | -55.36436 | 2025-06-04 04:53:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59304fbb-54ad-3237-890e-2b7249b60f3d | -14.01878 | -55.12938 | 2025-06-04 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f2de3fd-1503-37df-8cb5-6191e353d01c | -12.17258 | -64.20242 | 2025-06-04 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a2c4d95-c9ee-343d-b2ec-4532a87b5de5 | -11.80252 | -57.35364 | 2025-06-04 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a452d8fc-159d-3a63-9c36-ef693e54ab92 | -11.55737 | -56.41689 | 2025-06-04 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 496d532b-c4e7-3f26-87d0-5f42f29e9184 | -11.82293 | -57.81377 | 2025-06-04 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba5e572e-f1d3-3eb1-a68e-c2b11bdaea50 | -13.43035 | -47.53167 | 2025-06-04 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c31e6d97-593e-3191-876c-51a7fc40a77f | -15.07803 | -48.94532 | 2025-06-04 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5155d37e-16dc-3760-b452-dfd33c690b2a | -14.68343 | -52.68773 | 2025-06-04 04:53:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05812bed-dbab-3b34-9586-820aff4d12ee | -11.89668 | -56.40776 | 2025-06-04 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e32f295-f4e7-34d4-8dbe-cb2ac050f1f3 | -14.81743 | -48.46088 | 2025-06-04 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f221ada3-9450-3726-b726-2b49244c6ad7 | -13.9128 | -54.66011 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec2a91d0-adee-3fda-a7e3-c072f7fd74f5 | -13.90894 | -54.6631 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4424dc5e-6641-3aee-ad91-a687f585a3fd | -11.55672 | -56.42081 | 2025-06-04 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a64aa651-209e-3e65-a3cc-c02bf1ce40cc | -13.09284 | -52.02401 | 2025-06-04 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7afdd675-d652-3c01-8900-d96cb6766d2e | -11.82963 | -57.8196 | 2025-06-04 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 818fe4d2-a70e-3719-b72d-02f988dc4763 | -12.90585 | -55.04255 | 2025-06-04 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0488513c-dd6c-38be-ae85-70f7181856bf | -12.37803 | -54.16248 | 2025-06-04 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8801113-5a17-3df0-82a6-1d953cc965bd | -11.90107 | -54.78889 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README13.md)
