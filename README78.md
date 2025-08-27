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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11f96269-89d5-3d1b-93c6-a5830f279902 | -9.01438 | -65.69444 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91927666-5d75-31c8-8cff-27711e31f460 | -8.95194 | -65.96012 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c1707a24-2a84-3404-8d56-7b513a359ca5 | -9.08163 | -66.0632 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e82b6cc9-e96e-39c7-86b5-f9ad908323aa | -8.57858 | -70.11805 | 2025-08-27 05:46:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32a858aa-29e0-3d32-82c6-b3353943ea18 | -8.95416 | -65.96764 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 1ed17bef-967a-3691-baa6-5526a6d94f78 | -9.09088 | -65.72445 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e98f7eb7-e3a0-30d1-9a37-7485f0a4a72e | -8.96303 | -65.95473 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cbde1636-28aa-3673-8920-60bf1b4fb38a | -10.02841 | -59.3561 | 2025-08-27 05:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b29d12fc-85af-3a8c-baf8-c4bc0a679789 | -9.00391 | -65.39921 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37341256-cc1a-3a27-9914-59e79ab47bf2 | -8.10494 | -71.24819 | 2025-08-27 05:46:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a542cf70-d4c2-39b7-97a7-8b458a069423 | -10.4134 | -57.71099 | 2025-08-27 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19d1ad49-27a4-365e-8335-1be527f3892d | -9.59846 | -62.42371 | 2025-08-27 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0560dff9-53e5-3c4f-bc48-aa8f372eeae4 | -8.93421 | -65.94296 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| b5415535-45fe-3345-ba2a-363349720b2d | -8.94086 | -65.94402 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| adbfdc55-b40c-35ce-bf5c-26ed83d8cbc9 | -10.78074 | -60.79028 | 2025-08-27 05:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcc27977-456b-3537-af52-00ee74cf2c78 | -9.06444 | -66.06403 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 206823ac-1638-3465-821e-d7301345eb26 | -14.29992 | -60.36359 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08a3f192-99e0-34b9-9de2-1d61a533fec3 | -9.65412 | -64.99884 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2efe12c3-a2cd-3d0d-8d79-41b10e1bc155 | -9.03602 | -65.73011 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6eb3dd7c-419f-334a-8ce6-ca22ae08c7f2 | -8.96081 | -65.94722 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 94b87159-1820-3206-b2e9-c72ebf31e5bf | -10.52441 | -57.98622 | 2025-08-27 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26996e6e-2555-3940-a724-56263433c9f1 | -9.80172 | -64.26487 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d44e10a1-17ad-3a4d-9986-2efdbf6d61a4 | -10.15652 | -64.24636 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a0927e5-d31d-339b-9ddf-d52d60575d2d | -8.93421 | -65.92147 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b85268a-6e4f-3b12-992c-1d027a5101f6 | -8.95527 | -65.96066 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| dc0df02a-5865-3cc8-bea9-ae85b3f9be2e | -8.51777 | -69.79457 | 2025-08-27 05:46:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3dc9645c-435b-3bc8-9895-cb2325333f05 | -9.78804 | -64.24 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4861c2af-c5e3-3f66-bf8b-ad5570da8fca | -8.95582 | -65.95716 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| a67144d4-4e94-3058-89a8-ab21581f5963 | -8.9392 | -65.9545 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cc8ad39c-2972-3065-b635-e2dde899841f | -8.92964 | -65.93527 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ab4a077-f0c6-39b6-bfd7-d684808e568d | -9.28291 | -64.55604 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 80082d5e-4464-3e30-a5d6-0f823961da38 | -9.0711 | -66.0651 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 21b8e0e4-c2f1-3357-8aee-505c2866320a | -8.95748 | -65.94669 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 091dab73-522f-31b8-96ed-e48d8096967c | -8.96413 | -65.94775 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c969288b-e7d9-3d5a-af86-faea015a4aac | -9.83016 | -64.28444 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 292a8a36-30fe-35cc-b506-06934b1edd1c | -8.9252 | -65.92023 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7905c0b-df2f-3604-8872-2ceb940aeef6 | -8.49929 | -69.79902 | 2025-08-27 05:46:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e101fbd-ea21-351f-af86-b7e02913517f | -9.08756 | -65.72392 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a33659ef-37f2-31d2-b00f-9e74c954ea59 | -9.08201 | -65.71587 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72c976fc-8836-3a20-b3f8-e9a27fcf4020 | -14.77404 | -59.71601 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04386d8a-0d5e-35f1-b4e0-603da41306c2 | -10.03231 | -59.36127 | 2025-08-27 05:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54fc595a-72f5-3819-b9d8-1a751a35f6a8 | -8.99729 | -65.41969 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26b14b9b-c435-368c-b251-39420c51b5f1 | -14.30437 | -60.36439 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb340a68-3b7e-3f9e-be81-b172387683c0 | -8.92631 | -65.93474 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 284173e6-9a30-3696-b182-6b9056937e81 | -9.08478 | -65.71989 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca9487e9-eb56-3bc9-b111-aad0ec0f9d68 | -8.51611 | -69.79226 | 2025-08-27 05:46:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5582b50f-23c8-36e3-ab0e-ab9f04b76bf4 | -9.79831 | -64.26434 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf13daf2-36b9-3ebd-8eee-ec85fb592837 | -9.04932 | -65.73223 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f370a882-895b-3a9e-ac7e-6f50d53364fc | -14.31199 | -60.37604 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1405fdc4-1dd7-360f-9274-742ef16384ac | -10.77711 | -60.78593 | 2025-08-27 05:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8c33dd6-da34-3ad0-9779-022810459bc4 | -9.66082 | -64.99991 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4a4f100-f994-32ad-9681-820bf046aa7b | -8.95859 | -65.96119 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ebeed3e4-42c2-34bd-9eef-b0479cfb09d9 | -10.27069 | -64.50183 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e14dd24-b04a-3121-af83-c465512efdac | -9.02213 | -65.68851 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f089ce83-9667-3781-8058-12e2248c14d9 | -12.22323 | -64.22902 | 2025-08-27 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e3ee445-8020-3afd-94c0-4839a276ffcf | -9.32568 | -63.2037 | 2025-08-27 05:46:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 112362bd-f52d-3c16-8f3a-03675aab6762 | -8.51534 | -69.79698 | 2025-08-27 05:46:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f84fc9d1-8bb7-398d-af41-ff97c7d7abc3 | -8.95804 | -65.94319 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0f4d2ed1-af21-36ef-9419-f78f0a7aa891 | -10.08492 | -62.90808 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d2c7f54a-c176-33e4-b130-4046bafe5397 | -10.09638 | -62.90565 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 509edd47-1b93-30c0-8560-83b5d70251f9 | -9.06426 | -65.72388 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ef800ef-5410-311c-af59-7c43f957d72f | -8.9331 | -65.92846 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a2507c1-fff3-3c59-9796-404e3675d0fb | -11.30686 | -55.10894 | 2025-08-27 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe9922f1-fe3c-3996-bda9-ec902cfc4dbd | -14.30638 | -60.38426 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99dfb417-5003-3363-bb36-eacf5125b680 | -10.10787 | -62.90298 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c3bab74-877d-3f50-aca6-ccff0f10f20b | -8.93643 | -65.95048 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6e8ffa4f-3aa2-30b5-871d-38023254b4dc | -9.60993 | -64.44633 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3bf836d-51a9-3223-bba0-dfd4d85215c7 | -10.04202 | -64.94248 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f934703-0b3b-3ba3-ac93-34b584619157 | -12.2276 | -64.22859 | 2025-08-27 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30bfe9b2-f1aa-352f-a29f-f67b1730e0b5 | -9.79774 | -64.26804 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 368304f2-d3e1-3bc5-ab1e-54552261fe14 | -8.92852 | -65.92076 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36891448-c0c2-36f5-843a-63b9e0d6abc2 | -10.09849 | -68.98141 | 2025-08-27 05:46:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5266b421-9365-377c-8d59-3e7860b70c86 | -8.94308 | -65.95154 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 9613629d-1cb5-3691-993e-09ddaee79232 | -14.77551 | -59.71218 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 058c787f-0a57-3ed8-bbe8-2bf0d8f90658 | -9.065 | -66.06054 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc86ec31-b4ca-3f40-b0d3-25c5cf35a204 | -10.52447 | -57.98267 | 2025-08-27 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07d53e01-7bb5-3fdd-8602-85461bd723d8 | -8.93365 | -65.92496 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95516d21-d9a8-3780-bb31-ca6191cd7d0e | -9.28235 | -64.55966 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10aeeeb4-21db-3405-9eb7-51f9b878b621 | -9.13526 | -65.27244 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a56ccd90-b70f-3d60-bd4e-0570d5599c14 | -8.93255 | -65.93195 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02d34337-cdec-3b77-8fae-11aa4acbe445 | -9.64516 | -64.99014 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f26ab54-7ca6-386c-9f52-a68eacbeb01d | -8.94917 | -65.9561 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a15f9bd2-b357-38d6-b4bb-d1e823724d2a | -9.04322 | -65.72768 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e4213a6-b729-3b79-8926-127c7e87f62d | -9.01493 | -65.69093 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa8ccdc2-df51-351f-8f46-21c3efab68ba | -8.91855 | -65.91917 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 758505bd-4f27-37c6-bbaf-95d1c7349b1a | -9.06001 | -66.0705 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27971853-4365-33b9-b66e-28802603dee9 | -8.92908 | -65.93877 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e2a0e23-d470-3ce5-a549-cc4000696382 | -8.9464 | -65.95207 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| a10b6c85-9580-3d59-9c45-b3452defb8fc | -10.42238 | -64.3774 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f0f5cf6-745f-372c-936a-55ca2fcb1012 | -9.60654 | -64.44581 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f11e53b7-2eaf-3eaf-b5db-ac0a96c38983 | -9.07426 | -65.72179 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0194b04-83c3-3991-b4ac-3a101139cb57 | -10.03682 | -59.36197 | 2025-08-27 05:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 014f2c12-1e80-3091-b761-88eb9d612aff | -10.40871 | -57.70739 | 2025-08-27 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bde1c2b9-de9d-31c7-971b-3b820392438b | -9.13471 | -65.27596 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14406b7c-d77f-318b-8236-fbadbc1b1fb2 | -9.65187 | -64.9912 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6a0a6de-40d0-3b76-93f6-172530aee7d5 | -11.3063 | -55.11369 | 2025-08-27 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1c8f0be-9746-3f19-9d2a-b475565d900d | -8.59338 | -68.15022 | 2025-08-27 05:46:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5453137c-f499-3e31-b96e-03ff920deb00 | -9.79887 | -64.26064 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f44fbc69-a701-3a1c-8b98-2b19f131d33c | -8.95416 | -65.94615 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2ad107e-e7fa-35de-8dac-38fbaf152639 | -10.40874 | -64.39806 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README79.md)
