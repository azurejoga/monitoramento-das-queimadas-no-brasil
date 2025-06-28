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
| b5f2ee76-9557-3af3-8bc3-9a62fa85bf17 | -10.83436 | -53.75448 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f84dd3e9-cc08-3169-8fb0-7c61d124ea4a | -16.25726 | -53.68394 | 2025-06-28 05:44:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80ff411d-2ad8-3c82-bc84-bf0ef49274c6 | -11.05477 | -56.74669 | 2025-06-28 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3eb99928-9dd1-31a0-a04f-f35ba28669e8 | -10.30258 | -57.12943 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f925835c-fd03-386c-80d0-52cda563a674 | -10.29186 | -57.00125 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53fc4762-6a74-38b8-952d-ac067cc38e40 | -11.03855 | -55.37365 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 49ab2ad8-06a3-369a-bf41-3121af134d05 | -13.82974 | -59.67248 | 2025-06-28 05:44:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38b292cd-4ae4-3013-887b-ac51b1a04c72 | -10.83266 | -53.74773 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 807e39e8-18df-3cda-bf21-04a215a6f39e | -10.82702 | -53.75954 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ea16827-3ee2-38d6-ac36-66ee26db8915 | -9.09243 | -59.49432 | 2025-06-28 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8730a338-4c1e-35d6-b7ff-fab7a7200295 | -9.35689 | -58.85403 | 2025-06-28 05:44:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bc2a497b-b25a-36ad-ac37-e02a8bae00dc | -14.68933 | -53.38937 | 2025-06-28 05:44:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c8762692-ef77-3b94-880a-01d942c674b8 | -12.10358 | -54.58967 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e5387feb-ab66-3ef8-a640-cff388685ef3 | -11.04919 | -55.07772 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 27a60463-1514-3b32-bc29-7e8cfda1c4d2 | -12.50521 | -58.35768 | 2025-06-28 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42d7d47e-e4a0-31df-93dd-5362a19d05ae | -11.27425 | -52.74815 | 2025-06-28 05:44:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3dc2c435-3c47-3a32-bb7b-00fd8dd04c95 | -11.44212 | -54.48595 | 2025-06-28 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2e04be2-a542-3ae3-beb9-02bba4923ac6 | -11.05521 | -56.74305 | 2025-06-28 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b352d1e0-cdab-3683-99c5-69453cdfcd4a | -10.03703 | -59.36234 | 2025-06-28 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fd49d01-b629-326c-8ea7-de1cc87eacb6 | -11.2784 | -52.75301 | 2025-06-28 05:44:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9ddbc27e-edf0-3683-8bcb-49f9b85929a2 | -12.11118 | -54.59485 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a3efe439-8fc6-359f-b935-702a03304cb0 | -10.83366 | -53.76035 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8c59f0a9-a12b-373e-af9f-2f2b1fe8b193 | -9.92941 | -59.93917 | 2025-06-28 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 27628def-4e1c-3744-9f3c-4b030da2496d | -10.84529 | -53.75535 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca9095ff-4655-3b47-b8f1-8ca1c044e43a | -9.43844 | -63.45973 | 2025-06-28 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac6b4861-40a9-394b-93e3-a266d7d42325 | -9.44136 | -63.46423 | 2025-06-28 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d578e428-23ba-3554-a554-95fcb2da8857 | -11.06265 | -55.37702 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6fdcf538-a875-32e3-9b2c-74f83c8e2ab2 | -11.2713 | -52.75232 | 2025-06-28 05:44:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 00d1a459-7c7c-3365-b23b-2209b0c28ab3 | -11.05294 | -55.37139 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 41bcf73e-e5c1-3ed0-82da-c89be724e146 | -13.94304 | -54.48719 | 2025-06-28 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 292264d3-0b01-3f47-94df-93ea0b80d66a | -9.04048 | -63.98212 | 2025-06-28 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2011471-76a0-30f8-8327-fcd46e0ac66e | -9.60422 | -63.46679 | 2025-06-28 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95cc0ac7-b76b-34f9-8202-d99aa3424e99 | -9.60774 | -63.46733 | 2025-06-28 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4d74cf9-9fa1-323f-ac75-148fa4ac1389 | -9.09366 | -59.48535 | 2025-06-28 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0b5a29d-a7ef-3114-a3b8-88e6e3d49887 | -10.3017 | -57.13619 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0592c796-7623-3208-9574-0e957e024a9b | -12.02976 | -57.0882 | 2025-06-28 05:44:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87dece2a-50d5-3df3-b678-561df268c431 | -10.82174 | -53.74712 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 666bf438-3ad4-3998-9e4f-8a87a2cdbb0b | -12.11122 | -54.57992 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2bca511b-76f7-34ab-88fa-7f7483d64391 | -10.832 | -53.75371 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 561fac5e-a5c3-3783-82f8-a9be0736494b | -10.84694 | -53.76209 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8a1848c6-d24a-3b75-b64b-caf657be3ac6 | -12.10999 | -54.59054 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9e9cf045-2750-351b-9f30-5c236ffa3d9f | -15.15724 | -55.3497 | 2025-06-28 05:44:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f1b4176-b1d4-39ca-9a1a-72b5e3f36fd0 | -11.05663 | -55.37613 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dc830f0e-3109-32e8-8840-6d8db6029d3c | -10.83962 | -53.76694 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 13cfdfe9-eaa0-3b19-aff5-0686d29cc262 | -10.29593 | -57.13888 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0123df2-7dc9-3d5e-83c4-27591d126f49 | -11.60619 | -55.54576 | 2025-06-28 05:44:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| baa3552f-7bb4-3a74-8e48-1ff60b7bc066 | -11.05897 | -55.37228 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1fe10b98-6b65-3e0f-9fb9-f7d058f8de0e | -10.28561 | -57.00747 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 789118b8-9c27-3fd5-869c-5c2b779b5d2f | -11.05116 | -55.37075 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 4d488f82-5296-3006-859b-0380c07ae642 | -10.29098 | -57.00815 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc289ad8-6821-3048-b1b6-14ee830928be | -10.81217 | -57.74832 | 2025-06-28 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed3ed8f9-502b-306a-bea7-783174d9a272 | -10.83134 | -53.75957 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 96ac0fb2-054a-3916-95e7-2ce1b0f6ee12 | -10.82841 | -53.74776 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5cdabdee-3682-3c92-b537-c789d039e2c3 | -11.26715 | -52.74743 | 2025-06-28 05:44:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 58a14274-13d0-385b-b238-51c1dfc5bff8 | -9.72081 | -56.18447 | 2025-06-28 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1c00cc66-f31a-3f40-b550-1a96f2be2e50 | -10.82771 | -53.75373 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71515a5e-2e24-3362-a2f7-6a2ab71298a5 | -11.04882 | -62.58557 | 2025-06-28 05:44:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ec419c8-7551-31d1-9ec3-96b9731779f3 | -9.72129 | -56.18057 | 2025-06-28 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 74cd0dec-8b54-3d41-b1eb-ebb165fd0546 | -12.10944 | -54.67019 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 18534151-d371-35c0-a5c2-bbf2f1635338 | -11.27915 | -52.74601 | 2025-06-28 05:44:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 57120356-d35a-3c32-ad75-4301bd512581 | -12.10776 | -54.66573 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1826683d-48cd-35df-ae85-a061c86e458b | -12.1164 | -54.59135 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2484db57-4382-38f6-8b26-1b90714bdd72 | -10.04287 | -59.36088 | 2025-06-28 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf77f5e1-4c1f-3c9e-ab95-080f08b881ee | -11.88557 | -58.73851 | 2025-06-28 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b46edb2-dbf2-33bc-b7b8-71fb23ad0b8a | -10.81138 | -57.75462 | 2025-06-28 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7262a26a-e51f-3f17-a9c7-b36c189c9e2b | -11.05241 | -55.37603 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 67d46e19-a872-3943-b166-a5e29b21a3f6 | -11.05059 | -55.37539 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| f7051476-1f13-37a7-b41d-e22da66eeaf5 | -10.29637 | -57.13552 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb4bb1be-5eed-3ad2-a5bc-10f89d654f8f | -11.61591 | -58.28974 | 2025-06-28 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eeecbb3d-a5e6-3ce3-bb65-3e44df2ec274 | -10.30126 | -57.13958 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b39dba4-d7f5-36b3-8fe0-6318cc0ed5ad | -11.78219 | -59.31934 | 2025-06-28 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac9b88cc-90fa-3557-862f-9261b6489f92 | -10.81098 | -57.75772 | 2025-06-28 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 857df46d-ad7b-3202-acee-f4c191aa30bb | -14.6935 | -53.39064 | 2025-06-28 05:44:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7d6f2ebd-f72f-317b-b197-7742ccca0551 | -12.10419 | -54.58443 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 348c2c9d-7eee-3a44-8876-35abebba266c | -11.88208 | -58.72685 | 2025-06-28 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 377136eb-b425-3d31-9a99-e8eea7a37ab9 | -7.89014 | -61.46558 | 2025-06-28 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5b3396cd-4164-3238-b688-2686e1b6b76d | -9.08738 | -59.49806 | 2025-06-28 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a9d34fd-79cd-3529-a505-d6ab51f06269 | -10.05651 | -59.36298 | 2025-06-28 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6196be21-106b-3635-a1a6-255d746db2f8 | -13.94244 | -54.49271 | 2025-06-28 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 126e27bc-bb90-3db2-9e81-9966429799cf | -9.53343 | -63.57462 | 2025-06-28 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92ac7d25-3607-3f99-b84d-e6a8e5be21c4 | -12.50559 | -58.35471 | 2025-06-28 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89d43f4d-645c-3ccd-b808-1787a8c5c3b0 | -14.83833 | -59.8024 | 2025-06-28 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1399df02-ca4a-3884-bc53-bd196962a943 | -11.80842 | -56.96262 | 2025-06-28 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fd8293d-6445-3dc8-a9ad-3fec500545d6 | -13.13796 | -56.80793 | 2025-06-28 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6cd82b9-4a64-306c-a76d-f831f6a0d190 | -10.71034 | -59.13087 | 2025-06-28 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b16bfcf-e252-36a9-8034-b7c23bda9b74 | -10.83734 | -53.76621 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7b9e070d-f89b-3874-91da-0ca37637abde | -11.05003 | -55.38004 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 6b4d2c96-8c3b-36e1-a769-090215e45dce | -9.03705 | -63.9816 | 2025-06-28 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8909ffe3-30fb-3ec3-8cde-47a6df17eea3 | -10.29725 | -57.12871 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 796d0986-4d3d-3b8d-a5bc-2e1cbc16f8b6 | -11.80293 | -56.96181 | 2025-06-28 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e436ee69-4bfe-38c7-b213-6703092bac06 | -9.03647 | -63.98537 | 2025-06-28 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13dfd707-b47c-3bb7-b88e-5d0fbb2d3acc | -12.10938 | -54.59578 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9368c412-3c92-3352-9deb-cbb9a7b68a5c | -10.29681 | -57.13211 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d0b11ac-a451-389a-a014-eb607c052488 | -12.10534 | -54.58873 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 70af2d7e-f65a-36a4-82b2-9e168a79b93f | -10.83864 | -53.75454 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc7474d9-8cb5-3206-aa6b-b8a7d1b1d508 | -11.27057 | -52.75908 | 2025-06-28 05:44:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 4f29b9a0-776a-30d6-b663-fff330d0dc97 | -12.10592 | -54.58345 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8a7df11f-27ee-353a-aed5-923541487040 | -10.03833 | -59.36012 | 2025-06-28 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19cb3195-645e-3d53-9382-16204757d109 | -10.03069 | -54.32923 | 2025-06-28 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2059ff4d-917a-3f71-b5d2-754a3f447b2a | -9.36156 | -58.85472 | 2025-06-28 05:44:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README28.md)
