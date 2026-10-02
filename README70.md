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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6144d58e-342b-3299-bfc5-9bcfb74e5d0f | -13.33684 | -43.85838 | 2026-10-02 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be9bdfba-a518-3cee-8815-b7433ca4d8dc | -15.31574 | -42.78105 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 40e678c5-0ed7-3ee1-bfd1-15aaba9173c1 | -8.2357 | -55.27275 | 2026-10-02 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a4887cc-31b2-3b4f-8dba-f0076a1a7c97 | -8.41594 | -54.70478 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59b6cea4-8031-3e8b-ae66-b4934333652a | -15.52322 | -46.13336 | 2026-10-02 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 50d9ce47-f655-36ec-9c73-ec90b9534f92 | -15.31685 | -42.77398 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| da408eaf-79e1-3ff4-8e60-a8f2bd9725ce | -11.46432 | -43.41688 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e0b6edd-2006-3472-b408-fece05fa9e0c | -11.66515 | -43.60523 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0f39efc1-9984-3365-8d8b-aa58ceaead33 | -10.25373 | -49.66798 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61c3a421-3222-33d1-a040-4590b1d3bc75 | -9.51735 | -54.66919 | 2026-10-02 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 51c784d5-6a56-3c21-9a01-511738df04cf | -9.57832 | -54.62514 | 2026-10-02 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 875ffecc-e00d-386a-9fc4-b9c223993174 | -11.75086 | -43.57489 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 366eba27-0458-3e9b-aa7b-3d0505333f0d | -11.14741 | -44.60921 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c2d3610e-42b5-37cf-aecf-4fa62472e51d | -9.76501 | -53.80294 | 2026-10-02 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 946a99f3-f292-3364-b2d6-3b1ee215f378 | -10.9035 | -51.18696 | 2026-10-02 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9ab73b5e-afd2-3bef-93d1-2b7377f9c2db | -15.30854 | -42.78306 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 156.5 |
| ee2986af-9904-364a-b2a4-bd1fc04b4eae | -15.31797 | -42.75674 | 2026-10-02 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c3d6f278-17d1-3ac9-b409-a1a6b8289d38 | -8.30891 | -54.76244 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b53270b3-042c-3a68-8549-8caffa708c47 | -11.79583 | -43.57799 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1afe73c4-8b0c-31ec-a0b5-21d305cf0306 | -9.82739 | -44.81443 | 2026-10-02 04:59:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e3beb6d-c128-34e5-aa3d-2b5b85e29f2d | -13.34141 | -43.85728 | 2026-10-02 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c4095849-9210-3611-8e17-6c152891a541 | -11.14199 | -44.60409 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1f1845d1-176e-35e8-97ab-420724c7c9bd | -12.18428 | -57.10734 | 2026-10-02 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27a8561f-7a1e-3dd0-8443-652b605e53d9 | -15.52045 | -46.12706 | 2026-10-02 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ba9494c-f6f2-3209-beb1-3fb3e0697d7a | -15.30931 | -42.7748 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 267.2 |
| 1d08d456-756e-319a-965a-3a7e97bbf633 | -10.25176 | -49.66941 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89379f61-73c0-3d98-964b-04bd0a5845d3 | -10.21727 | -45.30664 | 2026-10-02 04:59:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 910042e7-9fbf-386a-ba2c-e1025204c299 | -11.23994 | -45.22933 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74d7ea2a-3e28-396a-b3b1-f9b317b98bc2 | -11.46955 | -43.42843 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 022366b4-0436-37b8-9149-9b0a9fb65c1c | -11.14793 | -44.60485 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2dd73b76-cb23-338e-9cc1-ff66e5a2d52f | -11.25133 | -45.23114 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d156ce5-e6ba-39c9-ae99-a708d9ab5631 | -11.66008 | -43.59348 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0e722559-b750-33ab-9fec-086a60ce67b1 | -13.34906 | -43.86519 | 2026-10-02 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d763843-d0a8-34b6-a87b-f2227077471c | -9.78914 | -53.82507 | 2026-10-02 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76caf12a-81bc-320c-acb5-3b05691353bf | -11.6882 | -43.59586 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6a5d43a-e470-3f5c-b37e-c216a014ab9e | -15.5208 | -46.12373 | 2026-10-02 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2ccb6e2-2edf-371a-aa93-2d9a58df5be2 | -13.8663 | -43.64731 | 2026-10-02 04:59:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7e07f542-5bdf-397c-88ae-2ee31c33a383 | -10.89928 | -51.18326 | 2026-10-02 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a9647d74-1fe3-3e8c-8fe9-7ada137ff690 | -15.31619 | -42.78066 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 306.0 |
| bc8f9295-b441-3060-85ac-eced29eaeffe | -15.32346 | -42.77364 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f52f2a53-d6f7-3f1c-8b15-c789fcc4294d | -11.72612 | -43.43238 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff6601d4-175e-3bff-b9d3-c729ea24ca00 | -8.31275 | -54.75949 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04967844-7582-34f2-b318-d90dc4e7325f | -11.15334 | -44.61008 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2db5b9c9-defc-3deb-a04b-a500f00c1f65 | -9.817 | -44.81347 | 2026-10-02 04:59:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75a272a6-2623-3aff-9245-1738937fd99c | -15.32363 | -42.77647 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 306.0 |
| 8a74253e-6a5f-3911-85f9-c19c2ec0cb83 | -11.64775 | -43.55257 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 25484ad2-0a83-3e71-be5c-7ab73411af57 | -11.76658 | -43.54962 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be03c29a-82a7-3ffd-8788-378791d29ffc | -9.78524 | -53.82816 | 2026-10-02 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e195167a-29f3-36ab-bdaf-de784b99885c | -11.78512 | -43.55781 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c699ad07-c472-3b00-9df3-2551b7872d19 | -12.53461 | -43.08776 | 2026-10-02 04:59:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| ae6ccbc4-1eb2-300d-8373-0df8d3382f36 | -21.90348 | -57.82058 | 2026-10-02 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| cd8bd360-51ab-3a49-b8dc-0666a245e8c0 | -21.90737 | -57.8175 | 2026-10-02 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 1f5b8c5d-33f5-34e7-a72c-ade9be31cbbc | -11.15 | -44.61 | 2026-10-02 05:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8d94fc7f-6b3d-39c5-b1e4-fb74e6b3a4c0 | 3.43071 | -51.27601 | 2026-10-02 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72a1c4e7-1296-3953-8ade-9165549eb3b5 | 2.54622 | -50.96389 | 2026-10-02 05:31:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 935f6848-dc2f-3f12-8d61-0b6399f33fcc | 2.55016 | -50.95796 | 2026-10-02 05:31:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7e8e5606-2a72-3001-bef1-6821db38cd35 | 2.55411 | -50.95203 | 2026-10-02 05:31:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bea6a77-0ac1-34d3-ba64-12a0814b588f | 2.55495 | -50.95718 | 2026-10-02 05:31:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 517b89c7-dce5-3ee8-9a0c-2d35a6296359 | 4.32513 | -59.98652 | 2026-10-02 05:31:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31522314-cd8e-3082-b68c-edf41a149ca3 | 3.43533 | -51.27524 | 2026-10-02 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a2f719be-c3d2-3a60-9f5e-c54483af487d | 2.54931 | -50.9528 | 2026-10-02 05:31:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 593b5174-7485-3ed9-9cc2-149aa372a7c4 | 4.32227 | -59.99074 | 2026-10-02 05:31:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bbee277-df7c-3179-80e3-56d38f0ad5e5 | 1.92351 | -50.88824 | 2026-10-02 05:31:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21d6398f-3623-3f8a-a252-5785d663335e | 4.32169 | -59.98704 | 2026-10-02 05:31:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e5acbad-ee69-3724-8cfe-e1cb36951a64 | 2.55101 | -50.9631 | 2026-10-02 05:31:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 64603fa7-f615-3edf-8d35-31b0280e4876 | -3.16692 | -54.10022 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cee3fb6d-8afb-3f8f-8595-f9968045800d | -2.89763 | -54.09011 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cf38ba2-71e4-3e54-9f1b-9be22e86b4ab | -3.02321 | -53.97254 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f1f37f52-40e9-3a75-b328-4369c3e01834 | -2.8971 | -54.14882 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce1cd84a-2b66-3c05-925b-6563ad87074e | -3.16564 | -54.07998 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9fb9106d-61b5-3ca7-940d-66bb7942323e | -3.18387 | -54.10257 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d535b449-c5b0-35bd-8560-b88572357554 | -5.37277 | -56.03595 | 2026-10-02 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae355902-e5b6-30c1-b278-8f531275e006 | -3.29947 | -53.84852 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d911c9a-d6a0-3555-a8eb-a8468b869fac | -4.42952 | -54.84907 | 2026-10-02 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8f3ffbd-1799-346c-aa71-41417198828b | -3.14315 | -53.75168 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5e0cd01-448f-398b-908c-7a5120c198f1 | -3.18811 | -54.10309 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d5f61fe-1df3-3e24-9935-56eb950cc591 | 2.00951 | -61.08476 | 2026-10-02 05:33:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a856357-ea4a-311c-bfad-237cac4837eb | -4.26468 | -50.75076 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ba05fd9-d817-3926-b684-c41b39a60db7 | -3.13079 | -53.74563 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5fd1d0d9-e6bc-3540-8062-ded350b2068c | -3.13017 | -53.74972 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1fb3c9b0-9519-39c9-825f-ec1b308e7154 | -3.28535 | -53.85459 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26ae5ef0-0879-31b4-bf91-e455a9c73c0c | -3.01956 | -53.96796 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ce596380-87c1-32e7-9cad-8e6290858a09 | -4.28555 | -50.76731 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57a65521-e32b-38a9-9655-86085b3fbedd | -3.01222 | -53.23157 | 2026-10-02 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78972416-5464-3cc9-90c8-ad276789300c | -4.26212 | -50.76786 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d95a77d-53b4-3244-abc2-e9c28cea7fba | -3.29517 | -53.84785 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d52dc899-3692-3544-8474-970e2d204376 | -3.17962 | -54.10207 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 10bb52a1-4e3a-3eed-8560-eb0d1f042dec | -4.28948 | -50.77844 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a7f7711-315c-3781-b222-323b1e5c33fe | -4.24948 | -50.74129 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb58edd6-e2ae-3dbd-baf5-1a363a7cce28 | -2.89409 | -54.14054 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ec727594-7632-3349-a74b-fbae854f3cda | -4.27447 | -50.75925 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62eaf605-c4a7-358b-a078-1b2d4648079c | -5.89487 | -53.49492 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d23cc1e9-2262-3355-804b-a6c7f488dad7 | -1.64413 | -55.13318 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d0bb467-5273-34cf-8aae-a1dd8bcf9c7e | -4.26671 | -50.73713 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| df348509-e48b-3435-ab02-4f38c3247547 | -6.15248 | -47.46177 | 2026-10-02 05:33:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4a4cb23-9321-3c1b-b80c-423659f88c3c | -3.14007 | -53.74285 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 21c50bdb-29d8-3e3e-8273-6f5e7c54708c | -3.16083 | -54.08322 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6aa73b0-9c45-345e-b8ff-0a503bcdb3a0 | -3.01671 | -53.23217 | 2026-10-02 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b574a733-6d91-32d4-8739-744d42f84a5e | -4.29403 | -50.7762 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89893289-b5ae-3dcd-8038-e35cca56c584 | -4.45028 | -54.89947 | 2026-10-02 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README71.md)
