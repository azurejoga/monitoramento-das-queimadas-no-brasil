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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ff9acdb-4f05-3072-a131-eb7c6ba2f0f6 | -5.45809 | -60.14317 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 75e334f6-fb6b-3514-9e71-0da9e065c0a4 | -6.70182 | -58.85384 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ec2e335d-4283-31f5-8527-3728c3b3f45c | -6.11049 | -59.93397 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d098e15c-0162-3c51-9576-b4181a3e5ec1 | -6.70674 | -58.81786 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 36cbb0f5-f70a-3d50-8c42-a0bdae1553c1 | -6.09871 | -59.92686 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e09e6a6-9900-3c81-8ba3-5a22e027d29a | -6.08908 | -59.95034 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 605c4c82-f7ea-325b-960a-df50f0a8507d | -5.92119 | -59.93563 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a203bb0-02b4-30f7-bca5-d203eef42ab7 | -6.06891 | -59.95792 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ac0fc21f-b878-37f4-9281-5516f49417a3 | -6.67212 | -58.81948 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ebdf22c3-0a08-367a-8e21-b3cad2972744 | -5.45186 | -60.13833 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 43bead29-2ac7-3e8c-a0ed-f11ccf3bc278 | -5.4506 | -60.14766 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b2f2222-90f2-39cd-9d98-102e86ed153c | -6.10356 | -59.93791 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdda02ac-3f66-3c35-a53e-29ba56c6431e | -6.11254 | -59.91924 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78f3a92c-beda-3528-8275-a12cbe08b94a | -6.07785 | -59.93923 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a546f787-974c-3190-a961-404057f1a1a9 | -5.44584 | -60.14142 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f510b3f4-41bb-3aa3-8a79-8bcbed055767 | -5.4465 | -60.13677 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 73e8c221-2e67-3d33-9c72-a8ec986a8534 | -6.06332 | -59.95223 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4807a11b-9dda-3295-8c5a-6af6e2351b64 | -6.09597 | -59.9466 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b777ec8-f02a-3201-9938-2bf55c8428af | -6.08483 | -59.93485 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff1d589e-cb6c-3939-ab77-78f211c65f3f | -5.92185 | -59.93073 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0578e25e-668f-3b08-a729-e37b97620098 | -5.73816 | -59.88882 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35dcaab5-dd4f-38fa-8d81-8009800dab3d | -6.70343 | -58.84207 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15cbd5f5-0ebb-32b5-bc6a-cdc940e289b4 | -6.11324 | -59.91424 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a295b867-cce2-31d2-9419-8986bbe103de | -6.66454 | -58.82468 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 313df6b5-a65a-3f63-b268-3b76b1fc7456 | -5.92414 | -59.93547 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e67bd1d-c146-39de-9f1d-7d29ab9e4f8c | -6.09043 | -59.94052 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7df67dfe-8521-3cb2-96b4-a111a9508339 | -5.92275 | -59.94526 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65f0eb2d-4ca6-30ff-9dcf-d016d1a1b65a | -6.1063 | -59.91816 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abf6985e-e181-387f-bc4e-e98bd0fd7a11 | -5.93037 | -59.93641 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4825220-057f-3b21-8fa5-079180f852b2 | -6.1098 | -59.9389 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45c0c7a6-cdee-3f13-86b6-0946808e1c30 | -6.07091 | -59.94334 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 26184623-7aa6-34b7-870a-900ac1bfbb69 | -6.69667 | -58.84125 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2325a4f-8b71-3d5e-9d0c-d7d02975d715 | -5.45249 | -60.13366 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 65f7a441-35aa-3af9-9e50-839e290a66e9 | -5.45799 | -60.13921 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0cc2ac43-4491-3efc-803e-1df6922aaab3 | -6.69774 | -58.84684 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4b7c3d03-d493-3121-b4d5-c2213b1deb7e | -5.45943 | -60.13385 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 96a4236a-cd94-3a56-a429-28f420878c48 | -5.45313 | -60.12897 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9b3e695b-bf95-3a62-913d-9dfbf8443196 | -6.71266 | -58.82487 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6511d5e-29a7-3c90-b562-255012bd5d27 | -5.93594 | -59.94208 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08e5aa3a-f713-3c3d-8274-1a878a93cebd | -6.06825 | -59.96273 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 19c435f1-6d8c-3012-b5ab-db4160221f33 | -6.07653 | -59.94886 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 17dc7325-860b-3485-adde-0225eb7c7d1d | -5.44518 | -60.14609 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ee30fafc-59d6-3d47-831b-40418b6b0927 | -6.10912 | -59.9438 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0d98e5b-950f-37e8-8e17-fecdd236367f | -6.08348 | -59.94467 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fe783cf4-0ddb-3ab3-94c7-aca1629a9452 | -5.46009 | -60.12917 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d28eac1f-7668-391e-b65a-faebd8036efb | -5.92809 | -59.93169 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fda5e529-ad72-3362-a89e-06694b1c66fc | -6.65188 | -58.81657 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6e6ecc1-b66a-3e47-962f-37a66b9a22af | -5.45123 | -60.14299 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 24d0bc74-d464-31e0-8f84-9357fc2d1061 | -6.08281 | -59.9495 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a4421ae-9de3-3d44-8735-b4ef19c7f180 | -6.07587 | -59.95366 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6c57b0fe-1a10-33c9-99bc-04d72271e747 | -5.93368 | -59.93745 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd25ecbd-456e-3858-8da7-8a2680854d9a | -6.65107 | -58.82262 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77d246bf-4f97-3776-9df0-e141f6b2a9df | -5.92483 | -59.93059 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fcaaa5c-446a-3f2c-b974-962bed574bab | -6.70589 | -58.82406 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 276382a7-ba61-399a-a998-c5debd14ca05 | -6.69071 | -58.83454 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 24c5d181-e0ba-3293-9442-aa52635115b3 | -6.71349 | -58.81878 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d9ebdc3-57c1-3601-9d87-f50506626d91 | -5.45736 | -60.14388 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| da53d009-3629-3f85-8ead-6846c453e9a2 | -5.93733 | -59.93229 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abf872ac-2d52-3a59-909b-b24552e9c073 | -5.45396 | -60.12831 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cbd9ab4f-4a59-3039-979c-a2b233081b20 | -6.08416 | -59.93976 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2138632d-53e7-3c34-b4b2-56d661b0aba4 | -6.70262 | -58.84798 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3ec51b3-f092-3735-a6e2-7e1eb54a53f3 | -5.45672 | -60.14855 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2420eb5b-2612-36c6-bf4f-22b56581dd2b | -5.4513 | -60.14695 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 70f062d0-ec98-3dd6-b152-1d2d073ed450 | -6.11186 | -59.92417 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| abb4a20d-84f2-310b-b206-910de35759cb | -6.71941 | -58.82584 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aecd483e-c40d-30de-874a-38de7ac0e2ee | -5.92968 | -59.94129 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a075d64-78a3-3632-ab62-34bdb6083304 | -5.45863 | -60.13453 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ec02a856-d5fa-3e43-b877-d53f9cb3b80e | -5.93664 | -59.93718 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8353b73a-d700-3f57-82c4-417395bd162b | -6.69747 | -58.83534 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8a41d870-c099-3c47-8305-a0821b382f8d | -6.10219 | -59.94773 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8acc513-1a17-3efd-a685-d6b04371e029 | -5.92677 | -59.94149 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e65528a-a51f-3bc2-86b9-8b789d1da4d0 | -6.06265 | -59.9571 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c18c4ad-187e-3bce-a83b-302eb1dc7748 | -6.65861 | -58.81763 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 38e56ca0-f84c-3067-9844-cfb0a9e18f97 | -6.07719 | -59.94408 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 24031359-2f5d-300b-bbc4-7ea6e7f4ec3b | -5.44716 | -60.13213 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7a4753f6-8bcd-3627-a765-1d5d219d70bb | -5.93435 | -59.93255 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5d4554c-adeb-35d4-a4f8-54ad57dd2997 | -6.72532 | -58.83284 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a470dc34-bf4e-3284-8c99-60af0482970c | -6.69587 | -58.84708 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a1a557a-acce-3f2d-b9e3-c690596723fa | -6.07454 | -59.96336 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 43407958-702c-3013-836e-6fdce3303e69 | -6.70084 | -58.8229 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 756248c3-acf7-38f5-b30b-23c448b13aa0 | -6.10287 | -59.94283 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d5c8476-64a0-385a-92d1-373bd214b8b4 | -5.73193 | -59.88779 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f6b2db1-f86a-343c-9245-33f8f8b84067 | -6.70003 | -58.82912 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5d6e18f4-c436-3eaf-be66-50dde85e5bbc | -6.69913 | -58.82319 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fdb2d8f8-4c9a-33cd-b942-1d9a716e78be | -6.10425 | -59.93292 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88958175-76fa-3d65-8cfe-b5f3f80f248f | -6.08148 | -59.95919 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3dd81cc8-837d-39e8-8fc4-d89aee9ed258 | -5.45876 | -60.13852 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 76c05f8b-0b2d-31fa-96dd-9864130861d9 | -5.45263 | -60.13766 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b4a05b46-acde-3f0a-839d-4b7cfa485a37 | -6.06957 | -59.9531 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 69137b01-25da-322b-83d9-2c423f7b8539 | -6.06398 | -59.94735 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f10aaf92-07cc-3762-be8a-421b4c31626e | -5.45743 | -60.14783 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 62901e56-5e55-3be8-a83c-d9f7531ffcef | -5.93107 | -59.9315 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 383b4225-bf35-34bc-a801-a49ff9d7904a | -5.45197 | -60.1423 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b4cd44b4-b2e8-3288-a72d-a873f9bdefd0 | -6.69238 | -58.82223 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6da06722-2d3e-3987-85e9-b38151beb83d | -6.72025 | -58.8197 | 2025-08-15 06:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a284508-11f5-30e1-a069-cdbcb123e56c | -6.09666 | -59.94166 | 2025-08-15 06:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 175c6107-4f64-3f97-a9a9-3f5d74ec5308 | -13.4757 | -56.6739 | 2025-08-15 06:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| fddbfabc-62b9-3eed-91b9-47c14c7b3521 | -6.0807 | -59.9465 | 2025-08-15 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 0a5c9f49-8883-3389-b902-010a4fc5134e | -5.455 | -60.1391 | 2025-08-15 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| efe7a037-733d-3665-92a9-9de701d8b1f1 | -13.4759 | -56.6537 | 2025-08-15 06:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |


[Clique aqui para ver as próximas entradas](README66.md)
