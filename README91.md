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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7879e350-9565-3c4a-aaa7-0402fa63c18b | -8.87162 | -62.44395 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f715dfd0-f7cc-3c1c-9fac-5d583db04659 | -9.17577 | -59.44929 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ec16383-3cb3-3af6-85aa-dd847968658b | -7.38642 | -64.36105 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b93b5432-2eee-3fb2-b23f-cf554f81ac41 | -8.98922 | -65.41992 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a845ceca-90ea-3854-a100-4bfd060ae300 | -8.57761 | -62.63248 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d791349-0248-3660-8b93-c05ca068e01c | -10.41787 | -64.37659 | 2025-08-26 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57ab0c9b-8eaa-358a-8a22-dec185987b06 | -9.23573 | -60.92195 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85828ab2-5569-366b-a4ac-2fc531f8e723 | -9.10428 | -62.67269 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb93d771-500f-3e5e-8c5c-d370973b84da | -8.98566 | -65.41572 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f122687-0c20-3ed1-a698-c32b30b3db45 | -9.02223 | -65.68581 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2392c9ad-a7ac-3a8c-9c49-c0729c74b8fc | -8.56623 | -62.62438 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14609cd6-cf74-3dac-806a-4e892eabc50e | -8.10714 | -62.88132 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ff0ba063-285c-3ad4-bfcf-dab05bb20554 | -7.38609 | -64.34518 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4e8d2e7e-a4ff-3762-9300-00e9bbaf5982 | -11.60452 | -63.49099 | 2025-08-26 06:03:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c8e651f-da56-38ac-8ba6-c84e0aea69fe | -9.18085 | -59.50612 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a7c7776-2e1c-33f9-84a7-b513d0d8ea49 | -8.24685 | -61.46027 | 2025-08-26 06:03:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5d21b14-a747-3a98-9b72-8a39294dcf7a | -7.39124 | -64.35769 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 389259a7-34f1-3417-aa57-6e23248edf34 | -9.16566 | -60.76886 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a362c3af-3f4f-3759-9a29-bd5cc4a2021e | -8.24726 | -61.45721 | 2025-08-26 06:03:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37b150e4-d45e-32e5-9cb4-8d003ae24def | -8.99083 | -63.64853 | 2025-08-26 06:03:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7fc9410-2c13-31c0-a20f-fef00eaba74b | -9.18186 | -59.45014 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0409fa45-44c8-371c-8569-8e1a182b2ae3 | -7.65685 | -63.52561 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf999a99-7701-3255-ab6c-7ce392a9759e | -9.23667 | -60.9145 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f4dadc4-ee0c-3505-87f3-d02e033b6cef | -9.04976 | -65.72173 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae866262-7f00-3327-90a8-b77349567019 | -8.85249 | -62.43553 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| b365130d-2fff-3b45-8c0b-3e5c8b403a17 | -7.89958 | -63.5223 | 2025-08-26 06:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d234f71-2b75-3052-8471-1e853ec339fd | -7.62637 | -61.03822 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 740beb7f-69d1-3f4f-ab2b-de7cdcfcb973 | -8.55571 | -62.62835 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ca3c4e4-0238-31f5-9db8-a85e9e63505f | -9.07601 | -66.06655 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c7cf83e-abb0-3a93-be20-f43b3c7652b3 | -9.63727 | -59.64157 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20a61982-7c3a-32eb-9c42-cf8540d5707d | -9.0721 | -66.06598 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7528a5a-2bb9-3432-9b51-daaa52aa5b90 | -8.98656 | -63.64022 | 2025-08-26 06:03:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e49832e-8de5-3bb4-9c57-625001dda100 | -9.06173 | -65.72355 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7876ae75-a42a-3284-8f28-5c5f8909ad76 | -9.17966 | -59.51536 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0456bf10-0385-3367-9ae5-88f87499cb6c | -7.3918 | -64.35371 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7bf7a04-d4ac-3124-911c-035296ce1713 | -9.25841 | -65.62266 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc6781c7-9639-3ea1-adc6-4d026247b5e0 | -8.83605 | -62.4448 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f55096aa-a95e-3414-a697-a083b83218f0 | -8.54295 | -62.64859 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3cd0c0f-a5ea-3fb0-903c-53d74f198277 | -8.08672 | -70.1932 | 2025-08-26 06:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d89f945a-c143-35e2-aa1f-12c762ab406e | -7.3844 | -64.34446 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 829c401d-f741-36c9-b729-039eb192e998 | -8.57406 | -63.92585 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a40a7ac-6cda-3179-993c-8c99ef6228ff | -10.38819 | -57.69593 | 2025-08-26 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da8e9346-e669-3eab-a67c-dc6ec85cbc18 | -8.34229 | -62.93837 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| daee614b-479a-36bb-87c6-10b815de0eea | -7.38431 | -64.35713 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d24e36d3-2a6c-31af-898e-479361fc8490 | -7.54935 | -63.84313 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 256b5d7b-a4e7-3ee5-9b7c-231ad5fd6d8d | -7.37957 | -64.34784 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ce2c4687-2e8a-36d5-88ea-94afcb1aeb3d | -10.42111 | -64.3861 | 2025-08-26 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93c0889f-158c-3180-aa3a-9f4191567d13 | -8.84676 | -62.44049 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| f4985451-1b93-3bae-aa75-6ec4eb0b00da | -10.24853 | -59.66541 | 2025-08-26 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ca3b41d-f15f-387d-a4ca-15cd25a05a19 | -9.04104 | -65.7257 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bae08470-4d1f-3770-bc83-f5e97998b385 | -9.06971 | -65.72475 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b9046a0-8d30-3456-ba14-7497d5ff25cb | -9.174 | -59.46315 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b08f8285-cad7-3105-b20b-230edfe69113 | -9.16893 | -59.55083 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 106ec178-5c7b-32bb-9ed1-b6a0fdf79673 | -9.16522 | -59.53173 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8054300e-d52d-3f3d-885b-4f9cd7948978 | -9.2362 | -60.91823 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d637f2eb-8e85-3600-bca5-090ef2b4e51e | -9.17849 | -59.52438 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f655b36f-547c-3690-9e51-ac4a6c1f1e34 | -7.38013 | -64.34385 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 03f57f91-813a-39bb-8d25-c1ba64d78de7 | -9.16166 | -60.77359 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a634805-6ba0-3af0-82bd-623b29b74031 | -9.13777 | -60.78213 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0d8eadd-fc85-3c6c-ad25-42a719240fd5 | -9.63838 | -59.63265 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7a3441b8-d48d-343c-8c30-84a9dff57cdf | -8.976 | -65.42529 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d47ab480-acc1-340d-bff0-c8af6f850f78 | -9.80006 | -64.26058 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f1fa52f-0676-3d2c-874f-c751ae6eaa22 | -8.96028 | -68.7971 | 2025-08-26 06:03:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13a09480-78c3-3e59-80ea-0a548bd5b306 | -12.3319 | -64.22901 | 2025-08-26 06:03:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 909a8800-de71-3537-8ab8-d5b7839f8f64 | -9.8045 | -64.26122 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93972719-f945-3c80-a4dd-89ef39ae6d7b | -8.85595 | -62.44753 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fdedd74b-ad05-3ebd-83a4-ef7515538109 | -9.02435 | -65.72852 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 369859df-e591-3d99-a480-3d6705c6b406 | -7.87958 | -63.00954 | 2025-08-26 06:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 14570f98-5798-34ff-95b5-1aa9000cb22b | -8.86589 | -62.44891 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 05e4f089-e86c-3f21-a5cf-f7a218e61aa6 | -8.12144 | -62.88337 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c2e7164-d20b-36da-800c-897c88b8f3e5 | -8.89339 | -62.47001 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ac48b258-d2f4-3dd7-98b5-44b5a13505c5 | -7.61845 | -61.04109 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 899afd15-a465-3539-a612-bc4908a034ba | -9.17673 | -59.53804 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9401bf06-9dfc-3f2b-825c-705987ab5dcc | -9.16463 | -59.53629 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92716c3c-5f0a-37d3-b16f-abd0d404919a | -7.62382 | -61.04187 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bb5c14b-cc77-3592-b366-a690698119f6 | -8.34314 | -62.93475 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2640b2ca-1b6a-362a-aeac-779af96c0bca | -7.54492 | -63.84249 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6f6c740-02de-3173-af64-4bf1be9ce4dd | -7.56199 | -63.84935 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8824c4c8-5d54-3503-b0c2-fc00fdfbf02b | -9.17809 | -60.80494 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f72a339-a7b9-335a-97fb-f6cc1eac5e09 | -9.23737 | -60.91385 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a58cfe39-060d-377c-94da-083b5b25119a | -9.81017 | -64.25307 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5c82bde0-6272-3f3c-a77e-b49f19f22842 | -9.0091 | -65.39714 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed103ea3-8562-3add-9726-7bd3f9f9f2b6 | -8.97194 | -65.42469 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9013258b-abe0-3a53-a6d1-1fa214f1debd | -9.25787 | -60.92524 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a5bf5691-b4a4-3dac-acbd-7c671f6542cb | -10.25435 | -59.11206 | 2025-08-26 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0eee2032-b5a4-3159-a4a8-a81f0e197e72 | -7.89036 | -63.01275 | 2025-08-26 06:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3b33a0df-ca16-3538-8850-d81982c50ed6 | -9.19069 | -60.79534 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6b164c1-04a0-3982-8a45-62986262855f | -9.01369 | -65.39412 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c519193-ec7b-39be-b820-6b904cd48612 | -7.38182 | -64.34457 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c703b065-39a4-38cb-8161-c923a1ab953d | -9.01881 | -65.38747 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9167f17f-eea0-3a83-a836-81221450a30c | -9.20922 | -59.43573 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7469cc9-0aea-3e06-b32c-9dceac7aeee5 | -8.98313 | -65.40435 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fdcb163-710f-3e22-bcd0-5c12823a6011 | -9.16422 | -60.78012 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f57baad-9b45-3ed5-8425-5c01c3af30ca | -7.65232 | -63.52495 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d9d38cd-663f-3be7-b3b4-60597376bc72 | -9.17953 | -60.7937 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 767bc9b0-76fd-3ff1-a6f6-72c425daa226 | -9.03632 | -65.73026 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 838b2a98-62f4-3952-be9f-f4c7e0aebc29 | -9.32749 | -63.19781 | 2025-08-26 06:03:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 382f2e7e-df11-35b7-aaa7-a04fec439e1d | -7.38916 | -64.35378 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed8b23cd-d3a3-3e17-a02a-8eb07da62a67 | -9.01202 | -65.70036 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16aa7cea-4396-3ed6-9a9c-219bf4933418 | -7.29469 | -59.66779 | 2025-08-26 06:03:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README92.md)
