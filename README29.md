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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73ec3f92-f5d0-3abf-91c4-336a2ccca0df | -12.54386 | -46.95483 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 351a4a2e-ea1d-3466-8754-15bb68aa109e | -8.34657 | -44.94748 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3e1ffe0-f187-372c-be9f-06de9fc94130 | -9.96431 | -48.33681 | 2025-08-16 04:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3396d103-0477-33e0-a267-eda1d44a299e | -6.56747 | -43.03267 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e53d4ae-ad17-3197-9b43-850b66b796fd | -13.6046 | -46.9139 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afc601fd-06c0-3640-bc29-b5e0d959419b | -8.94818 | -45.81128 | 2025-08-16 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98f4786f-b183-32cb-9599-99f872f98d53 | -11.3417 | -55.43651 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30c7061f-279a-3dd2-89fd-9bafff1a9f31 | -12.61439 | -46.93262 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19807f10-7f0f-39fc-896d-abba876292ed | -12.55826 | -46.96234 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| e6e8cadd-b756-39c0-b13d-8355d0b77af3 | -12.2993 | -50.01192 | 2025-08-16 04:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a28d43a5-b8a3-3121-a720-3c0feac96136 | -8.34587 | -44.95166 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0f7a9ac-d607-343f-a436-1690062a37ca | -12.46144 | -46.98756 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea883d7c-7781-3aa1-b173-2620d2508066 | -7.69048 | -48.0029 | 2025-08-16 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0012bb1-815d-379e-a818-9a86a66d0d39 | -8.18912 | -45.01833 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b1b9a97-7d09-351c-949e-3e07d059166e | -7.13258 | -43.90258 | 2025-08-16 04:10:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a91a05e-193d-37e3-8da7-05f2de669040 | -6.55095 | -43.04873 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ab98660-532c-34a4-ba94-337194c3e713 | -11.74559 | -44.94698 | 2025-08-16 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a761f32b-9791-3ca2-9d51-6622160326f2 | -12.53703 | -46.94899 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c189bb0-e7fa-384a-bcee-e26bff3b56b1 | -11.25838 | -50.47309 | 2025-08-16 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9be9278-60c8-349d-9fec-c6146f427284 | -12.55622 | -46.9515 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 1d91713f-0db4-34e9-bea9-a19678875fff | -9.17303 | -45.32177 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe174109-6dd3-3361-a555-29fa38629162 | -13.58324 | -46.97076 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 411f8009-c68c-39e5-962c-8063c3c59799 | -13.62052 | -46.91091 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc236fba-5a86-3dc6-af2d-b190579ebb52 | -8.1848 | -45.02196 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4caeb572-8c3a-349d-810a-f8338bc41f05 | -12.5985 | -46.97952 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf791d35-86af-3495-a8dd-0d2ce5660e83 | -12.61352 | -46.93769 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 87f67ac3-8a2f-366d-853f-4b813af1c0f2 | -12.5915 | -46.92906 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 3924f6e2-13b1-300c-b8a0-cf6aeb69cfc1 | -7.35995 | -43.83597 | 2025-08-16 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecfc0ab4-ab25-3f5a-b6bb-9363caa98592 | -11.35083 | -55.42563 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16c44990-5fc4-3155-a1c4-0c3233a0f7c1 | -8.19068 | -45.03167 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d5bf4b0-2c55-36de-b160-8f5364574e1f | -7.59844 | -45.20669 | 2025-08-16 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b43c7fcc-7937-31e3-b1cc-6784d486455d | -8.17321 | -45.02439 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ea4a748-4c51-30f7-9fd4-8e3810c8489e | -9.50324 | -37.7207 | 2025-08-16 04:10:00 | NPP-375D | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 19fe7a02-43ee-30cb-854a-4aac1ea057fc | -11.34294 | -55.43039 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc7d4c0d-8e41-3f01-959c-8eaa61007440 | -12.52987 | -46.9673 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0acfa0cf-420d-3932-bf18-3221faf31b04 | -12.84041 | -46.04349 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 541bd40d-ddae-347a-8fed-8b554934fd8e | -12.60426 | -46.94603 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b21461ae-1e91-39c3-9f1c-b7cd49de8960 | -12.47073 | -46.97942 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3173b86-165c-3479-86c0-19c51c1e0c16 | -13.58783 | -46.9666 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 438a9198-6af5-30a5-98d9-b72a2e659430 | -8.17753 | -45.02074 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f169dca-e931-3b8f-81c2-554bdb3f941f | -10.47436 | -44.34066 | 2025-08-16 04:10:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a220f43c-4749-383c-8910-0699fd9e2a4a | -6.76594 | -44.33677 | 2025-08-16 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a437020a-c12e-36b0-8d38-13531f3781ff | -11.34568 | -55.43061 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b929f0c-de16-3c61-bb1b-b302838b4603 | -9.85656 | -44.68637 | 2025-08-16 04:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a811313-3469-36c0-9b9c-a8c0c3ac168b | -12.56379 | -46.95312 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fc5c6424-6557-3625-811e-3d23dfd2f14e | -11.50923 | -47.24539 | 2025-08-16 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 932ce992-7dd1-363c-abe1-9f87e8c74e25 | -6.56397 | -43.05462 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43a1075f-06e9-341d-b8ca-0345ba59efca | -6.54473 | -43.04397 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f63bbba5-3c56-3593-bc24-a7954883bb6b | -8.18341 | -45.03046 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f373b87-5b01-3183-9058-d8bb3c6965b7 | -8.19112 | -45.03022 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4983abc9-f29b-3347-ae68-55bd84521667 | -12.46227 | -46.98279 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2ea6a19-55ed-349e-9f6e-ab60aa7a557f | -6.53936 | -44.54187 | 2025-08-16 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cfb749f-114e-3901-aff3-5b12e245c170 | -12.60511 | -46.94107 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 19080a60-8487-3186-8e77-a8a858d44971 | -11.35726 | -55.40831 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e3bdcbe-759c-37c5-8b20-c3fb721025b8 | -12.60232 | -46.98017 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cb78ac5-1ddd-3997-b5f2-54945b9015c1 | -12.62946 | -45.23651 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f65186d1-adc9-3905-ac11-1b31aa127815 | -6.11448 | -45.92232 | 2025-08-16 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| faa97bf9-a26a-3a5a-a572-6337327f3f69 | -12.82236 | -45.99678 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3491d82-bc8e-37b6-a54a-1a1dd3528d02 | -12.62464 | -45.24379 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4c14b7a-0730-3158-b552-ee73b995296c | -7.49473 | -44.90348 | 2025-08-16 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f659a05-356b-364e-8806-071aab317058 | -11.57323 | -44.85165 | 2025-08-16 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bcc5f18-bb7d-3619-b41a-1826c77d6b57 | -10.85185 | -45.22009 | 2025-08-16 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0df06b73-b1be-3925-9e3c-f53283ea31e4 | -12.56756 | -46.95403 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c8b96159-53c1-3b41-93c1-922aebb74a0e | -8.18748 | -45.02962 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 22db28c7-f2c5-3f5f-a00d-fabff6c4366a | -13.56586 | -46.95931 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 202ad4c6-3fb7-3508-b50f-c1dbf4cca19a | -12.45429 | -47.00601 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 598f4b11-2999-358a-8e02-87ac81e750b7 | -12.61333 | -45.22561 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba97f01c-2dd8-38c0-ba28-092afd18cad8 | -12.56465 | -46.94818 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1bad68d8-981a-3120-a565-8a38c2e88cfb | -12.81516 | -45.99546 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fff590c5-544f-3b18-94bf-155dcccc641d | -12.543 | -46.95974 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6c058d78-86d2-39b7-ad4c-fd8e2e5fffe0 | -9.99139 | -48.54173 | 2025-08-16 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3de0f1d0-942f-384e-a302-91cfe62781c2 | -7.01121 | -44.31728 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2c0080c-a7e2-37fc-ac02-c7dd395c2c48 | -5.92918 | -53.65054 | 2025-08-16 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 974dc0c4-8f5b-385e-971d-a4e3d7a9a2dc | -11.41699 | -44.6869 | 2025-08-16 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a096e6b1-9889-3f7c-b6f8-d81faadee96f | -13.60837 | -46.91438 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 774d0518-81ac-30f5-9239-c4367ce0db60 | -12.22898 | -41.38613 | 2025-08-16 04:10:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 24ffb70d-f656-3b69-8bba-0925b53a8e74 | -9.81102 | -48.54368 | 2025-08-16 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2f12946-eebf-346f-883e-7135cf03bb8f | -12.84187 | -46.0568 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00d264fc-9b5d-3cdd-a1a1-e04209ea16bf | -6.5459 | -43.03668 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63a15d62-d5e5-3959-89eb-1fd6b5721455 | -6.67887 | -43.76489 | 2025-08-16 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8814765-808d-3015-beea-aaae6b106e77 | -12.53833 | -46.96392 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 548a7cfe-f960-3b63-87f9-5026c4535ac8 | -10.96773 | -49.56804 | 2025-08-16 04:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1439ebc1-5552-3be6-bd85-95624ee445f4 | -13.3332 | -45.21724 | 2025-08-16 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 990af780-44f4-3569-a985-81bc67264691 | -12.61902 | -46.92843 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f400afa1-bf3e-39cb-9a36-305fd7476e1c | -12.80579 | -45.98517 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32e4295f-716b-3cfa-8cb9-a9daea944b2b | -7.40818 | -44.88613 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bae4275-2923-373a-b679-c6ef8157751a | -6.67539 | -43.76431 | 2025-08-16 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d98a479-a068-39c4-ada5-9459174f4ea4 | -8.18549 | -45.01772 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45f857db-69c9-3236-afbb-06b32c8bf8c0 | -9.85191 | -47.81649 | 2025-08-16 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83ab43ef-52f4-3e76-af37-d23f2217d6f6 | -8.18411 | -45.02621 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee52b098-f099-3880-a2be-7d20443a0e71 | -9.02678 | -46.59423 | 2025-08-16 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1484e564-5b13-38c8-95e6-8f1bc0e9127a | -9.36925 | -47.97922 | 2025-08-16 04:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30f403b2-411f-37a0-a248-3e0f4bc7c663 | -6.76883 | -44.34152 | 2025-08-16 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebee580a-6ebe-3220-9214-a25d33f088f2 | -11.65508 | -51.62503 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0abb2be8-2d62-37a6-9d3d-37600f09b242 | -9.18396 | -45.32362 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 84b17cba-9e40-3df2-bad2-95818b469bfe | -11.36162 | -55.44082 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c16fbaf3-73af-3e24-a11a-e48f9c4ace4d | -11.36264 | -55.41572 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b41a99f-9e7d-3e8a-be41-7a809f8fdce3 | -12.60722 | -46.9516 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a1a74ce2-7799-35da-957e-541da0fad64a | -6.60513 | -42.75269 | 2025-08-16 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5d43eab0-9b91-3141-858f-93ba910e1b65 | -7.40749 | -44.89032 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README30.md)
