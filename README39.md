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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 498ef752-c89f-35d0-a6b5-5c7327a85146 | -5.7675 | -45.10628 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79057614-66c3-388f-82d1-9d4a7973cf1f | -6.91004 | -41.72182 | 2026-09-18 04:19:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3fe87b16-6f50-388d-9886-7d75ee66f09d | -3.10502 | -48.69589 | 2026-09-18 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc3910aa-18fd-3d3c-885e-76e779725c56 | -4.51126 | -54.97898 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bdc41347-8a57-35c4-83b9-98c3e98c4372 | -7.12377 | -42.18837 | 2026-09-18 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 895806d6-a5e2-3612-b61a-56427a29ef5c | -3.03737 | -51.36852 | 2026-09-18 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d10ca8fa-f9d9-3980-932e-b8fad561641a | -7.20191 | -44.10364 | 2026-09-18 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3f94719-ce5b-3d0a-a99a-3c7de44a881b | -5.59163 | -48.10392 | 2026-09-18 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e9bc094-b8f9-393c-b3c1-3715730a047e | -4.568 | -42.94949 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ea637698-ddf9-3594-b6a6-0ae37f09eec5 | -3.57724 | -43.46629 | 2026-09-18 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f287916-dc64-35b3-a74c-d8995c2f202c | -4.88388 | -56.07182 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 40685f3a-e3be-3f11-82a1-1d5ff1980c5e | -7.81219 | -44.90598 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 88d2e48b-fc9c-3538-b3bb-de54f866947b | -1.49692 | -54.97334 | 2026-09-18 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f073ba3-6ef5-362a-a5c5-a718c648688b | -4.5607 | -42.95206 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f814d9f-305b-3627-b4c2-99bfbaebfb7a | -7.11028 | -49.95191 | 2026-09-18 04:19:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c3d32b2-60bc-3b3f-804a-0bb545b4a07d | -5.5516 | -35.75485 | 2026-09-18 04:19:00 | NOAA-21 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e7155250-8b01-3457-bff4-097cc1ca5974 | -8.8922 | -62.4107 | 2026-09-18 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| d4d4d100-2ef5-35f1-a217-f0dcb5937bdc | -11.33724 | -44.01741 | 2026-09-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b95b83e-15e9-3792-b0fb-2d9ab2259826 | -15.25792 | -47.93685 | 2026-09-18 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e09dd43-87d9-3c4d-b2ab-1b66ffdc180e | -14.17436 | -45.1944 | 2026-09-18 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 24b478ea-7ffd-31d2-b04e-dc2ca539bf17 | -8.43915 | -45.79092 | 2026-09-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0afb0e8d-f25d-3fb5-a5a8-d856eba58aea | -7.74904 | -54.75222 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80536ed4-c20c-37e9-8d2c-78d9c974ce63 | -10.66685 | -49.04672 | 2026-09-18 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63f842ae-19d8-3a9b-9e75-a6ca3d1c303e | -13.3564 | -46.29802 | 2026-09-18 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac0029f6-727c-3317-bdb5-db5baaaf8034 | -9.75232 | -46.09538 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2817bf9-8bf7-3f3d-8cf9-bf95235903c8 | -11.57896 | -46.89349 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46760658-acbf-3d9e-8abc-9e94c5e5497b | -11.29282 | -43.47226 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 961698ac-f5c2-35ca-b4aa-a8480cb2df9f | -13.6039 | -48.29781 | 2026-09-18 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7a53bbbf-c99f-36f8-bd0e-d63e0fd29cca | -9.94304 | -45.28668 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 707c6d3f-aa96-31d6-b393-59464c7130e8 | -14.33153 | -46.69704 | 2026-09-18 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e705f63-9b68-3792-a3a8-8865da7ed2d8 | -13.60675 | -46.93657 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d46ca125-3c25-3d7d-85e6-dcd45d9e2eaa | -12.53546 | -47.08393 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d5370fc1-8841-340e-8c8c-33184d7e938e | -11.47683 | -45.7244 | 2026-09-18 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae79db20-dd6e-3f27-b3e2-51763ab45365 | -8.32164 | -44.9762 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5378009-f0ad-3184-8219-7037c8f898a1 | -10.5413 | -44.84716 | 2026-09-18 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7fccf7e-1f91-3936-9a96-2b6e013556c2 | -8.52015 | -44.50674 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72f35133-66ba-3229-b39c-be915c529cc6 | -12.43195 | -50.67678 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e51aa62-a3ab-3988-b545-38789a999835 | -12.56874 | -47.08915 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85f12f3f-1ada-359c-8bb3-c459496c513e | -12.31614 | -50.76497 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ded50a5-1980-359e-9794-feae5c954c73 | -10.95363 | -54.09003 | 2026-09-18 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 033d9b88-9707-36b9-8d7a-c7ad6ba23bff | -11.55514 | -46.89319 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d48128e-8025-36f1-96ba-d68bbdb04c53 | -8.71397 | -44.88126 | 2026-09-18 04:21:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d66100c1-a25c-30f2-bc1c-16cb76424ee0 | -9.86704 | -46.50962 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8208273f-8b82-3b12-a7a2-46b2a209ded5 | -9.9425 | -45.29016 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ad65a9b-710b-3285-b02d-e7eb51d47081 | -10.62742 | -50.24116 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a8d47cd-b3ea-3182-a24b-2d269521e81c | -9.57539 | -46.56746 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da3730a8-5605-30dd-b077-cc22bed4c267 | -9.4861 | -54.47911 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 10e7d431-172d-3aae-848b-5580fb84b1bf | -8.29478 | -45.62901 | 2026-09-18 04:21:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 424b71e0-28c9-3b8a-899d-7611d62f0420 | -8.93388 | -51.46369 | 2026-09-18 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20e30c0d-729c-3275-9ebd-208126335861 | -12.41923 | -50.70485 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e5557dd-a2f9-3541-9c2a-50ad0359806a | -8.89994 | -44.97449 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1088072c-a2cc-3fb1-bb75-175543cdd827 | -11.27882 | -43.51834 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdfde66c-a902-3f58-867f-5a5504fc7001 | -10.11813 | -45.65049 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 89f414eb-06b2-365f-b0c9-a97b25e54ba1 | -8.27497 | -45.64726 | 2026-09-18 04:21:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7051e179-49db-34ee-bceb-e5ffe315b0ef | -12.39223 | -50.70007 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 932d964b-da0c-32b3-91ce-81bab469c242 | -10.3193 | -45.31764 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 016593e5-59b0-39ca-adeb-e9b1b3223f0b | -10.52035 | -46.72453 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5321be9-0fee-3acd-bd02-2a5c1d3abe6c | -10.62488 | -46.06376 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 207aefaf-6648-327c-88a1-5b828032c7bb | -9.59438 | -45.86589 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 61744043-d6f0-314c-8214-a543a861ee60 | -10.51978 | -46.72808 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a7eb4d0-bfbd-36b3-97fb-7757722545b8 | -12.26962 | -50.75672 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9090b259-f923-363c-8dff-f83d39f98311 | -11.31288 | -46.7697 | 2026-09-18 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 356461ab-0f51-371e-8fae-332dae187dba | -12.31307 | -47.96056 | 2026-09-18 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bee1eefe-4c13-38e5-8f3e-f40cad393671 | -12.5458 | -50.69425 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32a2e4ee-941b-3083-86b9-49fff6f8b202 | -11.27941 | -43.51441 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2615f641-1b4f-30df-aaea-3bb9c45f31f7 | -9.24389 | -45.9097 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9257243-080d-3097-9e6c-69c0bf7b830f | -9.91255 | -48.38765 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d802531-91cb-3137-ae9b-0a70f04b51b4 | -10.51759 | -46.72045 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 53d4d1e1-6631-3413-8598-1c6247f24684 | -9.91191 | -46.54919 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a446377-5122-35ed-ab32-218dd1ce0cc1 | -10.40547 | -48.67813 | 2026-09-18 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc934079-d734-3801-8458-626502dbe581 | -12.13223 | -45.15492 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 053e81bb-7d82-3215-acc4-9620edc54fad | -11.8757 | -47.58571 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7a951ce-c0ef-340d-9023-8bb28d4c5db2 | -9.59493 | -45.8624 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 958e979f-b5d8-3827-88cd-c6a2faa6159b | -12.551 | -50.71032 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2d5568a-f123-3b53-ad2d-6dc0822ffc38 | -14.22648 | -48.51358 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10c992f6-782d-33cc-8d81-cdf337f230cd | -9.75824 | -45.05307 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b013ad4-7782-3d54-bb19-c8a4c8f919b2 | -8.44584 | -45.83478 | 2026-09-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdfd298a-1766-3848-9d53-13e6f0f77a95 | -10.33085 | -45.3087 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 633deb75-06b4-356c-8823-945605b80487 | -12.29118 | -47.3563 | 2026-09-18 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41037154-004f-3a93-8ea4-433c024b438b | -9.45559 | -45.44767 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47f71326-6a48-3940-8a47-6a172ea1eb07 | -8.68213 | -45.43492 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a9b5ff3a-d969-3652-b59f-8808c60c077c | -9.59878 | -45.85944 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c68e5f4c-4cae-3d57-a19b-cab269be3fc9 | -11.31308 | -47.25803 | 2026-09-18 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfa519d1-91b9-3b11-926f-4b305ea82959 | -7.4982 | -55.00841 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5caf7e95-02f0-3c12-9d8f-250ca7713bed | -9.94465 | -45.34414 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8771281d-a31c-3a4b-9878-127f17045a3f | -11.35655 | -44.0773 | 2026-09-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0b5416d-5aa4-3d05-819d-b61c3e04916b | -12.40464 | -50.6972 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb5ba946-18c8-3f96-b2c1-287caf226059 | -12.2692 | -50.78229 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef5f6d6d-f4bc-36b1-af8f-e9f52abc1722 | -10.07482 | -45.64296 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 177e27b8-f787-3cfe-b4fd-cb3797d1dc7f | -12.5349 | -47.08749 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 25df65b8-93dd-3a36-bfb4-e8ac57d82562 | -12.13556 | -45.1555 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f37514cd-be37-3d48-b8ce-f08bf47b4677 | -8.9467 | -51.466 | 2026-09-18 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec148b52-a32b-37a7-94b6-587efb0939c6 | -14.80558 | -48.56131 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3ff6ccfc-0e14-3924-8d1d-6577f451d9b8 | -10.62797 | -50.26132 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41b0e75d-8d8a-3ed1-8b99-566fe263a859 | -14.93545 | -49.91467 | 2026-09-18 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4156aae-5c6d-38b3-b152-65c5e12f83a8 | -12.69421 | -43.91034 | 2026-09-18 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02410910-aca2-3d17-9849-a248938984da | -8.47792 | -46.88019 | 2026-09-18 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b377267-5249-3481-be25-cb978246b823 | -10.55129 | -44.84874 | 2026-09-18 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65397988-b488-310c-a93d-a9fbe88fc96a | -10.82396 | -46.13931 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41ac3fd2-fb0f-3692-8295-85986dad4621 | -12.99711 | -46.94144 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README40.md)
